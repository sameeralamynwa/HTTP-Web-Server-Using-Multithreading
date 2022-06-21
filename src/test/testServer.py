import sys

sys.path.insert(1, '../')

import server

class TestServer:
    def __init__(self):
        pass

    def testConnection(self):
        serverObject = server.Server()
        serverObject.listenPassively()
        serverObject.acceptFromClient()
        serverObject.sendMessage()
        print(serverObject.receiveMessage())
        

if __name__ == '__main__':
    testObject = TestServer()
    testObject.testConnection()