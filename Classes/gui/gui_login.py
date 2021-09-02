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
    QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from Classes.users.user_types import user_types 
from Classes.users.user import user
from Classes.users.guest import guest
from Classes.users.editor import editor
from Classes.users.admin import admin
from .gui_home import gui_home

class gui_login(QWidget):
    
    def __init__(self, appMgr):
        super().__init__()
        from Classes.appManager import appManager
        self.appMgr = appMgr
        self.setWindowTitle("Login")
        self.setFixedSize(500, 300)
        # self.setGeometry( 200, 200, 600, 400 )
        self.setObjectName("gui_login")
        self.center()
        self.initUI()
        self.home = None
    
    def initUI(self):
        main_layout = QGridLayout()
        main_layout.setSpacing(10)
        main_layout.setObjectName("main_layout")

        # lable header
        lb_header = QLabel()
        lb_header.setText("Offer Management Program")
        lb_header.setAlignment(Qt.AlignCenter)
        lb_header.setFont(QFont("Times", weight=QFont.Bold, pointSize=15))

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

        # login button
        bt_login = QPushButton("Login", parent=self)
        bt_login.clicked.connect(self.login_clicked)

        # lable about
        lb_about = QLabel("PLL – 2020-3 – Wael Al-Haddad", parent=self)
        lb_about.setAlignment(Qt.AlignRight)
        lb_about.setFont(QFont("Times", pointSize=10))

        # -----

        # header
        # lb_us | tb_us
        # lb_ps | tb_ps
        # bt_login
        # about

        main_layout.addWidget(lb_header, 1, 1, 1, 5)
        
        main_layout.addWidget(lb_us, 2, 2, 1, 2)
        main_layout.addWidget(self.tb_us, 2, 4)
        main_layout.setRowMinimumHeight(2, 50)
        
        main_layout.addWidget(lb_ps, 3, 2, 1, 2) 
        main_layout.addWidget(self.tb_ps, 3, 4)
        main_layout.setRowMinimumHeight(3, 50)

        main_layout.addWidget(bt_login, 4, 2, 1, 3)
        main_layout.setRowMinimumHeight(4, 70)

        main_layout.addWidget(lb_about, 5, 4, 1, 2)

        self.setLayout(main_layout)

    def login_clicked(self):
        res = self.appMgr.tryLoginUser(self.tb_us.text(), self.tb_ps.text())
        if res == str(user_types.deny):
            msg = QMessageBox()
            msg.setWindowTitle("login deny")
            msg.setText("username or password is incorrect")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
            return
        self.home = gui_home(self.appMgr, res)
        self.home.show()
        self.hide()

    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = gui_login()
    app.exec()