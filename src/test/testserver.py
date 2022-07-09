import sys

sys.path.insert(1, '../')

import server, webfilehandler, consts, clientthread, socket

class TestServer:
    def __init__(self):
        pass

    def testConnection(self):
        serverObject = server.Server('0.0.0.0', 1234)
        serverObject.setParameter(socket.SO_REUSEADDR, 1)

        serverObject.listenPassively()
        clientThreads = []
        while True:
            (clientSocketFD, (ip, portNumber)) = serverObject.acceptFromClient()
            print("Connection estabilished from " + clientSocketFD + " address " + ip + " and port " + str(portNumber))
            clientThread = clientthread.ClientThread(clientSocketFD, ip, portNumber)
            clientThread.start()
            clientThreads.append(clientThread)
        
        for thread in clientThreads:
            thread.join()

        serverObject.closeClientConnection()
        

if __name__ == '__main__':
    testObject = TestServer()
    testObject.testConnection()