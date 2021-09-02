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
    QComboBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from Classes.users.user_types import user_types 
from Classes.users.user import user
from Classes.users.guest import guest
from Classes.users.editor import editor
from Classes.users.admin import admin

class gui_chgPass(QWidget):
    
    def __init__(self, appMgr, user_account):
        super().__init__()
        from Classes.appManager import appManager
        self.appMgr = appMgr
        self.user_account = user_account
        self.setWindowTitle("Change Password")
        self.setFixedSize(400, 200)
        # self.setGeometry( 200, 200, 600, 400 )
        self.setObjectName("gui_chgPass")
        self.center()
        self.initUI()
        self.home = None
    
    def initUI(self):
        main_layout = QGridLayout()
        main_layout.setSpacing(10)
        main_layout.setObjectName("main_layout")

        # current password
        # lable 
        lb_ps = QLabel("Current Password")
        lb_ps.setAlignment(Qt.AlignCenter)
        lb_ps.setFont(QFont("Times", pointSize=12))
        
        # textbox 
        self.tb_ps = QLineEdit()
        self.tb_ps.setText("admin")
        self.tb_ps.setEchoMode(QLineEdit.Password)
        self.tb_ps.setObjectName("tb_ps")
        # -----

        # new password
        # lable 
        lb_nps = QLabel("New Password")
        lb_nps.setAlignment(Qt.AlignCenter)
        lb_nps.setFont(QFont("Times", pointSize=12))
        
        # textbox 
        self.tb_nps = QLineEdit()
        self.tb_nps.setText("admin")
        self.tb_nps.setEchoMode(QLineEdit.Password)
        self.tb_nps.setObjectName("tb_nps")
        # -----

        # add button
        bt_Save = QPushButton("Save", parent=self)
        bt_Save.clicked.connect(self.bt_Save_clicked)

        # -----

        # lb_us | tb_us
        # lb_ps | tb_ps
        # bt_login
        
        main_layout.addWidget(lb_ps, 1, 2, 1, 2) 
        main_layout.addWidget(self.tb_ps, 1, 4)
        main_layout.setRowMinimumHeight(1, 50)

        main_layout.addWidget(lb_nps, 2, 2, 1, 2) 
        main_layout.addWidget(self.tb_nps, 2, 4)
        main_layout.setRowMinimumHeight(2, 50)

        main_layout.addWidget(bt_Save, 3, 2, 1, 3)
        main_layout.setRowMinimumHeight(3, 70)

        self.setLayout(main_layout)

    def bt_Save_clicked(self):

        if self.tb_ps.text() == "" or self.tb_nps.text() == "":
            msg = QMessageBox()
            msg.setWindowTitle("error")
            msg.setText("empty password not allowed")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
            return
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
