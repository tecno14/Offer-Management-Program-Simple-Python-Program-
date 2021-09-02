# from ..appManager import appManager
from .guest import guest

class editor(guest):

    def __init__(self, appMgr, username, password):
        guest.__init__(self, appMgr, username, password)

    def __str__(self):
        return "editor"

    def edit(self, offer):
        offer.edit(self)