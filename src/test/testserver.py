import sys

sys.path.insert(1, '../')

import server, webfilehandler, consts

class TestServer:
    def __init__(self):
        pass

    def testConnection(self):
        webFileHandlerObject = webfilehandler.WebFileHandler('./index.html')
        serverObject = server.Server(1235)
        serverObject.listenPassively()
        serverObject.acceptFromClient()
        serverObject.sendMessage(consts.httpHeader + webFileHandlerObject.readWebFile(-1))
        print(serverObject.receiveMessage())
        

if __name__ == '__main__':
    testObject = TestServer()
    testObject.testConnection()