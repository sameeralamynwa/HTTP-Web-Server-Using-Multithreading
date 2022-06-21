class Client:
    def Client(self, portNumber = 80):
        clientSocketFD = socket.socket();

    def connectToServer(self):
        clientSocketFD.connect(('127.0.0.1', portNumber))

    def sendMessage(self):
        pass

    def receiveMessage(self):
        print(clientSocketFD.recv(1024).decode())
    
    def __del__(self):
        clientSocketFD.close();
