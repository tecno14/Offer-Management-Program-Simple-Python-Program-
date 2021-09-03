import os
import json
import jsons
from Classes.offers.categories import categories
from Classes.offers.offer import offer
from Classes.offers.tags import tags

class offerManager:

    def __init__(self, offersDir=".\\offers\\", offersData="offers.json"):
        self.__offers = None
        self.offersDir = offersDir
        self.offersData = offersData

    def save(self):
        with open(self.offersData, "w") as f:
            data = {}
            for i in range(len(self.__offers)):
                data[str(i)] = self.__offers[i].toJSON()
            json.dump(data, f, indent=4)

    def getAll(self):

        if not os.path.exists(self.offersDir):
            os.makedirs(self.offersDir)

        if self.__offers == None:
            # try:
                self.__offers = []
                with open(self.offersData) as f:
                    data = list(json.load(f).values())
                for i in data:
                    self.__offers.append(offer(i))
            # except:
            #     self.__offers = []
            #     self.save() 

        return self.__offers


    def searchByName(self, name): #offer name
        res = []
        for i in self.__offers:
            if name in i.name:
                res.append(i)
        return res

    def searchByCategory(self, category):
        lookFor = []
        for i in categories.getAllList():
            if category in str(i).replace('categories.',''):
                lookFor.append(i)
        
        res = []
        for o in self.__offers:
            for c in lookFor:
                if c in o.categories:
                    res.append(o)
                    continue
        return res
        
    def searchByTag(self, tag):
        lookFor = []
        for i in tags.getAllList():
            if tag in str(i).replace('tags.',''):
                lookFor.append(i)
        
        res = []
        for o in self.__offers:
            for t in lookFor:
                if t in o.tags:
                    res.append(o)
                    continue
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

    def addOffer(self, offer):
        self.__offers.append(offer)
        self.save()
        return True
