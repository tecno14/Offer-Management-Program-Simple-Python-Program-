import os
import sys
import uuid
import tempfile
import comtypes.client
from docx import Document
from docx.shared import Inches

class offer:
    def __init__(self):
        tmp = str(uuid.uuid4())
        while os.path.exists(tmp):
            tmp = str(uuid.uuid4())
        self.id = tmp
        self.path = ".\\offers\\{}.docx".format(self.id)
        if not os.path.exists(self.path):
            document = Document()
            document.add_heading('offer "{}"'.format(self.id), 0)
            document.save(self.path)
            # https://python-docx.readthedocs.io/en/latest/
            
        self.pdf = ".\\pdf\\{}.pdf".format(self.id)
        
        self.name = ""
        self.customerName = ""
        self.details = ""
        
        self.categories = []
        self.tags = []       
 
    def read(self, user_account):
        if not isinstance(user_account, guest):
            return str(user_types.deny)
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
        # myWord = win32com.client.Dispatch('Word.Application') 
        # wordfile = self.path
        # myDoc = myWord.Documents.Open(wordfile, False, False, True)
        # myWord.visible=1
        os.system(self.path)

    