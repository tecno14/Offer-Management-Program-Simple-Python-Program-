import os
import sys
import json
import uuid
import tempfile
import comtypes.client
from docx import Document
from docx.shared import Inches

from Classes.offers.tags import tags
from Classes.offers.categories import categories

class offer(object):
    def __init__(self, data={}):
        
        if bool(data):
            self.id = data["id"]
            self.name = data["name"] 
            self.customerName = data["customerName"]
            self.details = data["details"]
            self.categories = [categories[x] for x in data["categories"]]
            self.tags = [tags[x] for x in data["tags"]]

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

        self.path = ".\\offers\\{}.docx".format(self.id)            
        self.pdf = ".\\pdf\\{}.pdf".format(self.id)
        
    
 
    def read(self, user_account):
        if not isinstance(user_account, guest):
            return str(user_types.deny)
        self.createDoc()
        # convert to pdf with tmp file name
            # self.pdf = tempfile.mkstemp() + ".pdf"        
        in_file = self.path
        out_file = self.pdf

        word = comtypes.client.CreateObject('Word.Application')
        doc = word.Documents.Open(in_file)
        wdFormatPDF = 17
        doc.SaveAs(out_file, FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()
        os.system(self.pdf)

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