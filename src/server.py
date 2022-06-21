import consts


class Server:
    def Server(self, portNumber = 80):
        self.serverSocketFD = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocketFD.bind(('', portNumber))
        self.portNumber = portNumber

    def listenPassively(self):
        serverSocketFD.listen(consts.maxQueuedConnections)

    def acceptFromClient(self):
        self.clientSocketFD, self.clientAddress = serverSocketFD.accept()

    def sendMessage(self):
        clientSocketFD.send('Thanks for connecting'.encode())

    def receiveMessage(self):
        pass
    
    def __del__(self):
        serverSocketFD.close()
        clientSocketFD.close()

