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
    QDialog
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from Classes.users.user_types import user_types 
from Classes.users.user import user
from Classes.users.guest import guest
from Classes.users.editor import editor
from Classes.users.admin import admin

class gui_addUser(QDialog):
    
    def __init__(self, appMgr, user_account):
        super().__init__()
        from Classes.appManager import appManager
        self.appMgr = appMgr
        self.user_account = user_account
        self.setWindowTitle("Add User")
        self.setFixedSize(400, 200)
        # self.setGeometry( 200, 200, 600, 400 )
        self.setObjectName("gui_addUser")
        self.center()
        self.initUI()
        self.home = None
    
    def initUI(self):
        main_layout = QGridLayout()
        main_layout.setSpacing(10)
        main_layout.setObjectName("main_layout")

        # username
        # lable 
        lb_us = QLabel("Username")
        lb_us.setAlignment(Qt.AlignCenter)
        lb_us.setFont(QFont("Times", pointSize=12))

        # textbox 
        self.tb_us = QLineEdit()
        self.tb_us.setText("admin")
        self.tb_us.setObjectName("tb_us")
        # -----

        # password
        # lable 
        lb_ps = QLabel("Password")
        lb_ps.setAlignment(Qt.AlignCenter)
        lb_ps.setFont(QFont("Times", pointSize=12))
        
        # textbox 
        self.tb_ps = QLineEdit()
        self.tb_ps.setText("admin")
        self.tb_ps.setEchoMode(QLineEdit.Password)
        self.tb_ps.setObjectName("tb_ps")
        # -----

        #type
        #lable
        lb_type =  QLabel("type")
        lb_type.setAlignment(Qt.AlignCenter)
        lb_type.setFont(QFont("Times", pointSize=12))

        # combo
        self.cb_type = QComboBox()
        self.cb_type.addItem("admin")
        self.cb_type.addItem("editor")
        self.cb_type.addItem("guest")

        # -----
        # add button
        bt_addUser = QPushButton("Add", parent=self)
        bt_addUser.clicked.connect(self.bt_addUser_clicked)

        # -----

        # lb_us | tb_us
        # lb_ps | tb_ps
        # bt_login

        main_layout.addWidget(lb_us, 1, 2, 1, 2)
        main_layout.addWidget(self.tb_us, 1, 4)
        main_layout.setRowMinimumHeight(1, 50)
        
        main_layout.addWidget(lb_ps, 2, 2, 1, 2) 
        main_layout.addWidget(self.tb_ps, 2, 4)
        main_layout.setRowMinimumHeight(2, 50)

        main_layout.addWidget(lb_type, 3, 2, 1, 2) 
        main_layout.addWidget(self.cb_type, 3, 4)
        main_layout.setRowMinimumHeight(3, 50)

        main_layout.addWidget(bt_addUser, 4, 2, 1, 3)
        main_layout.setRowMinimumHeight(4, 70)

        self.setLayout(main_layout)

    def bt_addUser_clicked(self):
        userType = "user_types.{}".format(str(self.cb_type.currentText()))
        if userType == str(user_types.admin):
            userType = user_types.admin
        elif userType == str(user_types.editor):
            userType = user_types.editor
        elif userType == str(user_types.guest):
            userType = user_types.guest
        else:
            msg = QMessageBox()
            msg.setWindowTitle("error")
            msg.setText("username type not found")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
            return
        res = self.user_account.tryAddUser(self.tb_us.text(), self.tb_ps.text(), userType)
        if str(res) == str(user_types.deny):
            msg = QMessageBox()
            msg.setWindowTitle("error")
            msg.setText("username used or you don't have permission to add user")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
            return
        print("add user done return:")
        print(res)
        self.close()

    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
