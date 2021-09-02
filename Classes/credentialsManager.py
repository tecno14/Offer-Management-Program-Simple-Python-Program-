import json
import os
from pathlib import Path
import hashlib
from Classes.users.user_types import user_types
from Classes.users import user, guest, editor, admin

class credentialsManager:
    
    Password = "Password"
    Permission = "Permission"

    def __init__(self, secret="secret", filepath="credentials.json"):
        self.__secret = secret
        self.filepath = filepath
        self.__data = None
        self.getAll()
        
    def to_md5(self, password, permission):
        source = password + str(permission) + self.__secret
        return str(hashlib.md5(source.encode(errors='ignore')).hexdigest())

    def __save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.__data, f, indent=4)

    def getAll(self, username="", password=""):
        if self.__data == None:
            if os.path.exists(self.filepath):
                with open(self.filepath) as f:
                    self.__data = json.load(f)
            else:
                self.__data = {
                    "admin" : {
                        credentialsManager.Password : self.to_md5("admin", user_types.admin),
                        credentialsManager.Permission : str(user_types.admin)
                    }
                }
                self.__save() 

        # if self.tryLoginUser(username, password) != str(user_types.admin):
        #     return {}

        
        return self.__data

    def tryAddUser(self, my_username, my_password, user_username, user_password, permission=user_types.guest):
        if user_username in self.__data or not isinstance(permission, user_types):
            return user_types.deny

        # if self.tryLoginUser(my_username, my_password) != str(user_types.admin):
        #     return user_types.deny

        self.__data[user_username] = {
            credentialsManager.Password : self.to_md5(user_password, permission),
            credentialsManager.Permission : str(permission)
        }
        
        self.__save()
        return self.__data[user_username][credentialsManager.Permission]

    def tryUpdateUser(self, username, oldpassword, newpassword):
        if username not in self.__data:
            return user_types.deny

        if self.__data[username][credentialsManager.Password] != self.to_md5(oldpassword, self.__data[username][credentialsManager.Permission]):
            return user_types.deny

        self.__data[username][credentialsManager.Password] = self.to_md5(newpassword, self.__data[username][credentialsManager.Permission])
        self.__save()
        
        # return self.__data[username][credentialsManager.Permission]
        return self.tryLoginUser(username, newpassword)

    def tryLoginUser(self, username, password):
        res = self.__data.get(username, {}).get(credentialsManager.Password, "")
        if self.__data.get(username, {}).get(credentialsManager.Password, "") != self.to_md5(password, self.__data.get(username, {}).get(credentialsManager.Permission, "")):
            return str(user_types.deny)
        permission = self.__data[username][credentialsManager.Permission]
        return permission
        