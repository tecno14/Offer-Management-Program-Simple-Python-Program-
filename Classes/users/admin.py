# from ..appManager import appManager
# from .guest import guest
from .editor import editor

class admin(editor):

    def __init__(self, appMgr, username, password):
        editor.__init__(self, appMgr, username, password)

    def __str__(self):
        return "admin"

    def tryAddUser(self, user_username, user_password, userType):
        return self.appMgr.tryAddUser(self.username, self._password, user_username, user_password, userType)
