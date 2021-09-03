import sys
import threading

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QGridLayout,
    QDesktopWidget,
    QLineEdit,
    QMessageBox,
    QAbstractItemView,
    QTableView,
    QComboBox,
    QHeaderView
)
from PyQt5.QtCore import Qt, QAbstractTableModel, pyqtSignal
# SIGNAL = pyqtSignal
from PyQt5.QtGui import QFont

from Classes.users.user_types import user_types 
from Classes.users.user import user
from Classes.users.guest import guest
from Classes.users.editor import editor
from Classes.users.admin import admin
from Classes.gui.gui_addUser import gui_addUser
from Classes.gui.gui_chgPass import gui_chgPass
from Classes.gui.gui_newOffer import gui_newOffer
from Classes.gui.gui_editOffer import gui_editOffer
# from Classes.appManager import appManager

class gui_home(QWidget):

    def __init__(self, appMgr, user_account):
        super().__init__()
        # self.setFixedSize(700, 400)
        self.setGeometry(100, 100, 700, 400)
        self.center()
        self.setWindowTitle("Home - ({})".format(str(user_account)))
        self.setObjectName("gui_home")
        self.appMgr = appMgr
        self.user_account = user_account
        self.initUI()
  
    def initUI(self):
        main_layout = QGridLayout()
        main_layout.setSpacing(10)
        main_layout.setObjectName("main_layout")

        self.is_admin = False
        self.is_editor = False
        if isinstance(self.user_account, admin):
            self.is_admin = True
        if isinstance(self.user_account, editor):
            self.is_editor = True

        # lable header
        lb_header = QLabel()
        lb_header.setText("Welcome {}".format(self.user_account.username))
        lb_header.setAlignment(Qt.AlignLeft)
        lb_header.setFont(QFont("Times", pointSize=10))

        # tb search
        self.tb_search = QLineEdit()
        self.tb_search.setText("search here")

        # lable header
        lb_searchBy = QLabel()
        lb_searchBy.setText("Search by")
        lb_searchBy.setAlignment(Qt.AlignRight)

        # combo
        self.ByNameOfOffer = "Name of offer"
        self.ByCustomerName = "Customer name"
        self.ByCategory = "Category"
        self.BtTag = "Tag"

        self.search_type = QComboBox()
        self.search_type.addItem(self.ByNameOfOffer)
        self.search_type.addItem(self.ByCustomerName)
        self.search_type.addItem(self.ByCategory)
        self.search_type.addItem(self.BtTag)

        # search button
        self.bt_search = QPushButton("Search", parent=self)
        self.bt_search.clicked.connect(self.lb_searchBy_clicked)

        # lable Current offers
        lb_currOffer = QLabel()
        lb_currOffer.setText("Current offers")
        lb_currOffer.setAlignment(Qt.AlignLeft)


        # Add User button
        bt_addUser = None
        if self.is_admin:
            bt_addUser = QPushButton("Add User", parent=self)
            bt_addUser.clicked.connect(self.bt_addUser_clicked)

        bt_newOffer = None
        bt_editOffer = None
        if self.is_editor:
            # New offer button
            bt_newOffer = QPushButton("New offer", parent=self)
            bt_newOffer.clicked.connect(self.bt_newOffer_clicked)

            # Edit button
            bt_editOffer = QPushButton("Edit", parent=self)
            bt_editOffer.clicked.connect(self.bt_editOffer_clicked)
            bt_editOffer.setEnabled(False)
            self.bt_editOffer = bt_editOffer

            # edit Document button
            bt_editOfferDoc = QPushButton("Edit offer document", parent=self)
            bt_editOfferDoc.clicked.connect(self.bt_copyOfferDoc_clicked)
            bt_editOfferDoc.setEnabled(False)
            self.bt_editOfferDoc = bt_editOfferDoc

        # make copy button
        bt_copyOffer = QPushButton("Read offer document", parent=self)
        bt_copyOffer.clicked.connect(self.bt_copyOffer_clicked)
        bt_copyOffer.setEnabled(False)
        self.bt_copyOffer = bt_copyOffer

        # Change My password button
        bt_chgPass = QPushButton("Change my password", parent=self)
        bt_chgPass.clicked.connect(self.bt_chgPass_clicked)


        # table
        self.header = ['Name', 'Customer Name', 'Details', 'Categories', 'Tags']
        data_list = []
        self.lastSelectedOffer = None

        table_model = MyTableModel(self, data_list, self.header)
        self.offers_view = QTableView()
        self.offers_view.setModel(table_model)
        # set font
        font = QFont("Courier New", 9)
        self.offers_view.setFont(font)

        # set column width to fit contents (set font first!)
        self.offers_view.resizeColumnsToContents()    
        # enable sorting
        # self.offers_view.setSortingEnabled(True)
        # SingleSelection
        self.offers_view.setSelectionMode(QAbstractItemView.SingleSelection)
        # full line selection
        self.offers_view.setSelectionBehavior(QAbstractItemView.SelectRows)

        header = self.offers_view.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        
        main_layout.addWidget(lb_header, 1, 1)

        main_layout.addWidget(self.tb_search, 2, 1)
        main_layout.addWidget(lb_searchBy, 2, 2)
        main_layout.addWidget(self.search_type, 2, 3)
        
        main_layout.addWidget(self.bt_search, 3, 3)
        main_layout.addWidget(lb_currOffer, 3, 1)

        main_layout.addWidget(self.offers_view, 4, 1, 1, 3)

        bt_list = QVBoxLayout()
        if self.is_admin:
            bt_list.addWidget(bt_addUser)
        if self.is_editor:
            bt_list.addWidget(bt_newOffer)
            bt_list.addWidget(bt_editOffer)
            bt_list.addWidget(bt_editOfferDoc)
        bt_list.addWidget(bt_copyOffer)
        bt_list.addWidget(bt_chgPass)
        
        main_layout.addLayout(bt_list, 1, 4, 4, 1)

        self.refrech_offers()
        self.setLayout(main_layout)
    
    def lb_searchBy_clicked(self):
        searchQuery = self.tb_search.text()
        if searchQuery == "":
            self.refrech_offers()
            return
        #     msg = QMessageBox()
        #     msg.setWindowTitle("error")
        #     msg.setText("search empty")
        #     msg.setIcon(QMessageBox.Critical)
        #     msg.setStandardButtons(QMessageBox.Ok)
        #     x = msg.exec_()
        #     return

        searchType = self.search_type.currentText()
        if searchType == self.ByNameOfOffer:
            self.refrech_offers(self.appMgr.searchByName(searchQuery))
        elif searchType == self.ByCustomerName:
            self.refrech_offers(self.appMgr.searchByCustomerName(searchQuery))
        elif searchType == self.ByCategory:
            self.refrech_offers(self.appMgr.searchByCategory(searchQuery))
        elif searchType == self.BtTag:
            self.refrech_offers(self.appMgr.searchByTag(searchQuery))
        

    def bt_addUser_clicked(self):
        self.add_user = gui_addUser(self.appMgr, self.user_account)
        self.add_user.exec()

    def bt_newOffer_clicked(self):
        self.newOffer = gui_newOffer(self.appMgr, self.user_account)
        self.newOffer.exec()
        self.refrech_offers()

    def bt_copyOfferDoc_clicked(self):
        if self.lastSelectedOffer == None:
            self.bt_editOffer.setEnabled(False)
            self.bt_copyOffer.setEnabled(False)
            self.bt_editOfferDoc.setEnabled(False)
            return
        self.tCopyDoc = threading.Thread(target=self.user_account.edit(self.lastSelectedOffer))
        self.tCopyDoc.start()

    def bt_editOffer_clicked(self):
        if self.lastSelectedOffer == None:
            self.bt_editOffer.setEnabled(False)
            self.bt_copyOffer.setEnabled(False)
            self.bt_editOfferDoc.setEnabled(False)
            return
        self.editOffer = gui_editOffer(self.appMgr, self.user_account, self.lastSelectedOffer)
        self.editOffer.exec()
        self.refrech_offers()
    
    def bt_copyOffer_clicked(self):
        if self.lastSelectedOffer == None:
            self.bt_editOffer.setEnabled(False)
            self.bt_copyOffer.setEnabled(False)
            self.bt_editOfferDoc.setEnabled(False)
            return
        self.tCopy = threading.Thread(target=self.user_account.read(self.lastSelectedOffer))
        self.tCopy.start()
        
    def bt_chgPass_clicked(self):
        self.gui_chgPass = gui_chgPass(self.appMgr, self.user_account)
        self.gui_chgPass.exec()


    def refrech_offers(self, offerSource=None):

        if offerSource == None:
            offerSource = self.user_account.getAllOffers()

        data_list = []
        for offer in offerSource:
            
            offer_categories = ', '.join([str(x).replace('categories.', '') for x in offer.categories])

            offer_tags = ', '.join([str(x).replace('tags.', '') for x in offer.tags])

            # ['Name', 'Customer Name', 'Details', 'Categories', 'Tags']
            data_list.append((
                offer.name, 
                offer.customerName, 
                offer.details, 
                offer_categories,
                offer_tags,
            ))
        
        table_model = MyTableModel(self, data_list, self.header)
        self.offers_view.setModel(table_model)
        self.offers_view.selectionModel().selectionChanged.connect(self.on_selectionChanged)

    def on_selectionChanged(self, selected, deselected):
        self.bt_editOffer.setEnabled(False)
        self.bt_copyOffer.setEnabled(False)
        self.bt_editOfferDoc.setEnabled(False)
        self.lastSelectedOffer = None
        for i in list(set([i.row() for i in self.offers_view.selectionModel().selectedIndexes()])):
            self.lastSelectedOffer = self.user_account.getAllOffers()[i]
            self.bt_editOffer.setEnabled(True)
            self.bt_copyOffer.setEnabled(True)
            self.bt_editOfferDoc.setEnabled(True)
            
    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.header)
        # if len(self.mylist) > 0:
        #     return len(self.mylist[0])
        # else:
        #     return 0

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    # def sort(self, col, order):
    #     """sort table by given column number col"""
    #     self.emit(SIGNAL("layoutAboutToBeChanged()"))
    #     self.mylist = sorted(self.mylist,
    #                          key=operator.itemgetter(col))
    #     if order == Qt.DescendingOrder:
    #         self.mylist.reverse()
    #     self.emit(SIGNAL("layoutChanged()"))
