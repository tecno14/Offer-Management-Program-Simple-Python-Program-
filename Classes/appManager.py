import sys
from random import randint
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
    QLineEdit
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from Classes.credentialsManager import credentialsManager
from Classes.users.user import user
from Classes.users.guest import guest
from Classes.users.editor import editor
from Classes.users.admin import admin
from Classes.users.user_types import user_types 
from Classes.offers.offerManager import offerManager
from Classes.gui.gui_login import gui_login
from Classes.gui.gui_home import gui_home

class appManager:

    def __init__(self, credentialsMgr, offerMgr):
        self.__credentialsMgr = credentialsMgr
        self.__offerMgr = offerMgr


    def getAllCredentials(self, username, password):
        # if not isinstance(credentialsMgr.tryLoginUser(my_username, my_password), admin):
        #     return str(user_types.deny)
        return self.__credentialsMgr.getAll(username, password)

    def tryAddUser(self, my_username, my_password, user_username, user_password, userType):
        # check that is admin
        if not isinstance(self.tryLoginUser(my_username, my_password), admin):
            return str(user_types.deny)
        return self.__credentialsMgr.tryAddUser(my_username, my_password, user_username, user_password, userType)

    def tryUpdateUser(self, username, oldpassword, newpassword):
        return self.__credentialsMgr.tryUpdateUser(username, oldpassword, newpassword)

    def tryLoginUser(self, username, password):
        permission = self.__credentialsMgr.tryLoginUser(username, password)
        user = None
        if permission == str(user_types.admin):
            user = admin(self, username, password)
        elif permission == str(user_types.editor):
            user = editor(self, username, password)
        elif permission == str(user_types.guest):
            user = guest(self, username, password)
        else:
            user = str(user_types.deny)
        return user


    def getAllOffers(self, username, password):
        if not isinstance(self.tryLoginUser(username, password), guest):
            return str(user_types.deny)

        return self.__offerMgr.getAll()

    def addOffer(self, username, password, offer):
        if not isinstance(self.tryLoginUser(username, password), editor):
            return str(user_types.deny)
        
        return self.__offerMgr.addOffer(offer)

    def saveOffers(self):
        self.__offerMgr.save()

    def searchByName(self, name):
        return self.__offerMgr.searchByName(name)

    def searchByCategory(self, category):
        return self.__offerMgr.searchByCategory(category)

    def searchByTag(self, tag):
        return self.__offerMgr.searchByTag(tag)

    def searchByTags(self, tags):
        return self.__offerMgr.searchByTags(tags)

    def searchByCustomerName(self, name):
        return self.__offerMgr.searchByCustomerName(name)


    def startGUI(self):
        app = QApplication(sys.argv)
        gui = gui_login(self)
        gui.show()
        app.exec()

