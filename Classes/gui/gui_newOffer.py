import sys
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
    QComboBox,
    QListView
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem

from Classes.users.user_types import user_types 
from Classes.users.user import user
from Classes.users.guest import guest
from Classes.users.editor import editor
from Classes.users.admin import admin

from Classes.offers.categories import categories
from Classes.offers.tags import tags

class gui_newOffer(QWidget):
    
    def __init__(self, appMgr, user_account):
        super().__init__()
        from Classes.appManager import appManager
        self.appMgr = appMgr
        self.user_account = user_account
        self.setWindowTitle("New Offer")
        #self.setFixedSize(400, 200)
        self.setGeometry( 200, 200, 600, 400 )
        self.setObjectName("gui_newOffer")
        self.center()
        self.initUI()
        # self.home = None
    
    def initUI(self):
        main_layout = QGridLayout()
        main_layout.setSpacing(10)
        main_layout.setObjectName("main_layout")

        # name
        # lable 
        lb_name = QLabel("Name")
        lb_name.setAlignment(Qt.AlignCenter)
        # textbox 
        self.tb_name = QLineEdit()
        # ----- 
        # customer name
        # lable 
        lb_custName = QLabel("Customer name")
        lb_custName.setAlignment(Qt.AlignCenter)
        # textbox 
        self.tb_custName = QLineEdit()
        # -----
        # details
        # lable 
        lb_det = QLabel("Details")
        lb_det.setAlignment(Qt.AlignCenter)
        # textbox 
        self.tb_det = QLineEdit()
        # -----
        # categories
        # lable 
        lb_cat = QLabel("Categories")
        lb_cat.setAlignment(Qt.AlignCenter)
        # box 
        self.model_cat = QStandardItemModel()
        self.listView_cat = QListView()
        for cat in [categories.mobile_app, categories.website, categories.microservice]:
            item = QStandardItem(str(cat).replace('categories.',''))
            item.setCheckable(True)
            # check = \
            #     (QtCore.Qt.Checked if checked else QtCore.Qt.Unchecked)
            item.setCheckState(Qt.Unchecked)
            self.model_cat.appendRow(item)
        self.listView_cat.setModel(self.model_cat)

        # ----- 
        # tags
        # lable 
        lb_tags = QLabel("Tags")
        lb_tags.setAlignment(Qt.AlignCenter)
        # box 
        self.model_tag = QStandardItemModel()
        self.listView_tag = QListView()
        for cat in [tags.e_commerce, tags.delivery, tags.maps, tags.tracking]:
            item = QStandardItem(str(cat).replace('tags.',''))
            item.setCheckable(True)
            # check = \
            #     (QtCore.Qt.Checked if checked else QtCore.Qt.Unchecked)
            item.setCheckState(Qt.Unchecked)
            self.model_tag.appendRow(item)
        self.listView_tag.setModel(self.model_tag)
        # -----

        # save button
        bt_Save = QPushButton("Save", parent=self)
        bt_Save.clicked.connect(self.bt_Save_clicked)
        # -----

        # lb_name           self.tb_name
        # lb_custName       self.tb_custName
        # lb_det            self.tb_det
        # lb_cat            self.tb_cat
        # lb_tags           self.tb_tags
        # bt_Save

        main_layout.addWidget(lb_name, 1, 2, 1, 2);     main_layout.addWidget(self.tb_name, 1, 4)
        main_layout.addWidget(lb_custName, 2, 2, 1, 2); main_layout.addWidget(self.tb_custName, 2, 4)
        main_layout.addWidget(lb_det, 3, 2, 1, 2);      main_layout.addWidget(self.tb_det, 3, 4)
        
        main_layout.addWidget(lb_cat, 4, 2, 1, 2);      main_layout.addWidget(self.listView_cat, 4, 4, 2, 1)
        main_layout.addWidget(lb_tags, 6, 2, 1, 2);     main_layout.addWidget(self.listView_tag, 6, 4, 2, 1)
        
        main_layout.addWidget(bt_Save, 8, 2, 1, 3)
        
        self.setLayout(main_layout)

    def bt_Save_clicked(self):

        if self.lb_name.text() == "" or self.lb_custName.text() == "" or self.lb_det.text() == "":
            msg = QMessageBox()
            msg.setWindowTitle("error")
            msg.setText("empty fields not allowed")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
            return

        cats = []
        for i in range(self.model_cat.rowCount()):
            if self.model_cat.item(i).checkState() == QtCore.Qt.Checked:
                cats.append()

        res = self.user_account.tryUpdateUser(self.tb_ps.text(), self.tb_nps.text())
        if str(res) == str(user_types.deny):
            msg = QMessageBox()
            msg.setWindowTitle("error")
            msg.setText("current password not match")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
            return
        print("change password return:")
        print(res)
        self.user_account = res
        self.close()

    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
