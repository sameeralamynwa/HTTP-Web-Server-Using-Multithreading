import socket, consts

class Server:
    def __init__(self, ip = '', portNumber = 80):
        self.serverSocketFD = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocketFD.bind((ip, portNumber))
        self.portNumber = portNumber
    
    def setParameter(self, key, value):
        self.serverSocketFD.setsockopt(socket.SOL_SOCKET, key, value) 

    def listenPassively(self):
        self.serverSocketFD.listen(consts.maxQueuedConnections)

    def acceptFromClient(self):
        self.clientSocketFD, self.clientAddress = self.serverSocketFD.accept()
        return self.clientSocketFD, self.clientAddress

    def sendMessage(self, messageFromServer = 'Thanks for connecting'.encode()):
        self.clientSocketFD.sendall(messageFromServer)

    def receiveMessage(self):
        return self.clientSocketFD.recvall()#.decode()
    
    def closeClientConnection(self):
        self.clientSocketFD.close()
    
    def __del__(self):
        self.clientSocketFD.close()
        self.serverSocketFD.close()