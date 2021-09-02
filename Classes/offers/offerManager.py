import os
import json
from .categories import categories
from .tags import tags

class offerManager:

    def __init__(self, offersDir=".\\offers\\", offersData="offers.json"):
        self.__offers = None
        self.offersDir = offersDir
        self.offersData = offersData

    def __save(self):
        with open(self.offersData, "w") as f:
            json.dump(self.__offers, f, indent=4)

    def getAll(self):

        if not os.path.exists(self.offersDir):
            os.makedirs(self.offersDir)

        if self.__offers == None:
            try:
            #if os.path.exists(self.offersData):
                with open(self.offersData) as f:
                    self.__offers = json.load(f)
            #else:
            except:
                self.__offers = []
                self.__save() 

        return self.__offers

    def searchByName(self, name): #offer name
        res = []
        for i in self.__offers:
            if name in i.name:
                res.append(i)
        return res

    def searchByCategory(self, category):
        category = str(category)
        res = []
        for i in self.__offers:
            if category in i.categories:
                res.append(i)
        return res
        
    def searchByTag(self, tag):
        tag = str(tag)
        res = []
        for i in self.__offers:
            if tag in i.tags:
                res.append(i)
        return res
    
    def searchByTags(self, tags):
        tags = [str(x) for x in tags]
        res = []
        for i in self.__offers:
            if all(item in tags for item in i.tags):
                res.append(i)
        return res

    def searchByCustomerName(self, name):
        res = []
        for i in self.__offers:
            if name in i.customerName:
                res.append(i)
        return res

    def addOffer(self, offer, user_account):
        if not isinstance(user_account, editor):
            return str(user_types.deny)
        self.__offers.append(offer)
        self.__save()