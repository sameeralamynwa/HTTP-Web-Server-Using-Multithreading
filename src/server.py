import socket, consts

class Server:
    def __init__(self, portNumber = 80):
        self.serverSocketFD = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocketFD.bind(('', portNumber))
        self.portNumber = portNumber

    def listenPassively(self):
        self.serverSocketFD.listen(consts.maxQueuedConnections)

    def acceptFromClient(self):
        self.clientSocketFD, self.clientAddress = self.serverSocketFD.accept()
        return self.clientSocketFD, self.clientAddress

    def sendMessage(self, messageFromServer = 'Thanks for connecting'.encode()):
        self.clientSocketFD.sendall(messageFromServer)

    def receiveMessage(self):
        return self.clientSocketFD.recv(1024)#.decode()
    
    def __del__(self):
        self.clientSocketFD.close()
        self.serverSocketFD.close()