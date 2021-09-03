import os
import sys
import json
import uuid
import tempfile
import threading
from shutil import copyfile
import comtypes.client
import win32com.client

from docx import Document
from docx.shared import Inches

from Classes.offers.tags import tags
from Classes.offers.categories import categories

from Classes.users.user import user
from Classes.users.guest import guest
from Classes.users.editor import editor
from Classes.users.admin import admin
from Classes.users.user_types import user_types 

class offer(object):

    tmpCopyFile = os.path.abspath(".\\tmp.doc")

    def __init__(self, data={}):
        if bool(data):
            self.id = data["id"]
            self.name = data["name"] 
            self.customerName = data["customerName"]
            self.details = data["details"]
            self.categories = [categories[x.replace("categories.","")] for x in data["categories"]]
            self.tags = [tags[x.replace("tags.","")] for x in data["tags"]]

            self.path = data["path"]
            self.pdf = data["pdf"]
            return

        tmp = str(uuid.uuid4())
        while os.path.exists(tmp):
            tmp = str(uuid.uuid4())

        self.id = tmp
        self.name = ""
        self.customerName = ""
        self.details = ""  
        self.categories = []
        self.tags = []   

        self.path = '"{}"'.format(os.path.abspath(".\\Offers\\{}.doc".format(self.id)))
        self.pdf = '"{}"'.format(os.path.abspath(".\\Pdf\\{}.pdf".format(self.id)))
        
    def read(self, user_account):
        if not isinstance(user_account, guest):
            return str(user_types.deny)
        
        if os.path.exists(offer.tmpCopyFile):
            os.remove(offer.tmpCopyFile)
        copyfile(self.path, offer.tmpCopyFile)

        # with open("\"{}\"".format(self.path), 'rb') as f, open("\"{}\"".format(offer.tmpCopyFile), 'wb') as g:
        #     while True:
        #         block = f.read(16*1024*1024)  # work by blocks of 16 MB
        #         if not block:  # end of file
        #             break
        #         g.write(block)
        
        # convert to pdf with tmp file name
            # self.pdf = tempfile.mkstemp() + ".pdf"        
        
        # self.createDoc()
        # word = win32com.client.DispatchEx('Word.Application')
        # doc = word.Documents.Open(self.path)
        # wdFormatPDF = 17
        # doc.SaveAs(self.pdf, FileFormat=wdFormatPDF)
        # doc.Close()
        # word.Quit()
        os.system(offer.tmpCopyFile)

    def edit(self, user_account):
        if not isinstance(user_account, editor):
            return str(user_types.deny)
        self.createDoc()
        # myWord = win32com.client.Dispatch('Word.Application') 
        # wordfile = self.path
        # myDoc = myWord.Documents.Open(wordfile, False, False, True)
        # myWord.visible=1
        os.system(self.path)

    def createDoc(self):
        if not os.path.exists(self.path):
            document = Document()
            document.add_heading('offer "{}"'.format(self.name), 0)
            document.save(self.path)
            # https://python-docx.readthedocs.io/en/latest/

    def toJSON(self):
        data = {}
        data["id"] = self.id
        data["name"] = self.name
        data["customerName"] = self.customerName
        data["details"] = self.details
        data["categories"] = [str(x) for x in self.categories]
        data["tags"] = [str(x) for x in self.tags]

        data["path"] = self.path
        data["pdf"] = self.pdf

        return data