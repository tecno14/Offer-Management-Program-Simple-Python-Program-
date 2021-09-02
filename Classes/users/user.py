# from ..appManager import appManager
from .user_types import user_types

class user:

    def __init__(self, appMgr, username, password):
        self.appMgr = appMgr
        self.username = username
        self._password = password

    def __str__(self):
        return "user"
    # def tryLoginUser(self, username, password):
    #     return self.appMgr.tryLoginUser(username, password) != str(user_types.deny)

    def tryUpdateUser(self, confirmPass, newPass):
        res = self.appMgr.tryUpdateUser(self.username, confirmPass, newPass)
        if res == str(user_types.deny):
            return str(user_types.deny)
        
        # self._password = newPass
        return res

