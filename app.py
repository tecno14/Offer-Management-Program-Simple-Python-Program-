import pprint

from Classes.users.user_types import user_types
from Classes.appManager import appManager
from Classes.credentialsManager import credentialsManager
from Classes.offers.offerManager import offerManager

def start():

    credentialsMgr = credentialsManager(secret="123", filepath=".\\credentials.json")
    
    # print("change admin password")
    # print(credentialsMgr.tryUpdateUser("admin", "admin", "pass"))

    # print("add guest")
    # print(credentialsMgr.tryAddUser("admin", "pass", "guest1", "g1", user_types.guest))
    # print("add editor")
    # print(credentialsMgr.tryAddUser("admin", "pass", "editor1", "e1", user_types.editor))
    # print("add admin")
    # print(credentialsMgr.tryAddUser("admin", "pass", "admin1", "a1", user_types.admin))

    # print("login as guest")
    # print(credentialsMgr.tryLoginUser("guest1", "g1"))

    # pprint.pprint(credentialsMgr.getAll("admin", "pass"))

    appMgr = appManager(credentialsMgr, offerManager())

    appMgr.startGUI()

if __name__ == "__main__":
    start()