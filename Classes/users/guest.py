import win32com.client, pythoncom, time

# from ..appManager import appManager
from .user import user

class guest(user):

    def __init__(self, appMgr, username, password):
        user.__init__(self, appMgr, username, password)
    
    def __str__(self):
        return "guest"

    def getAllOffers(self):
        return self.appMgr.getAllOffers(self.username, self._password)
	
    def searchByName(self, name):
        return self.appMgr.searchByName(name)

    def searchByCategory(self, category):
        return self.appMgr.searchByCategory(category)

    def searchByTag(self, tag):
        return self.appMgr.searchByTag(tag)

    def searchByTags(self, tags):
        return self.appMgr.searchByTags(tags)

    def searchByCustomerName(self, name):
        return self.appMgr.searchByCustomerName(name)
    
    def read(self, offer):
        offer.read(self)
