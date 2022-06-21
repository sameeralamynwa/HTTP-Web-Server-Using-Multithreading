import socket

class Client:
    def __init__(self):
        self.clientSocketFD = socket.socket()

    def connectToServer(self, portNumber = 80):
        self.clientSocketFD.connect(('127.0.0.1', portNumber))

    def sendMessage(self, messageFromClient = 'Thanks for accepting'):
        self.clientSocketFD.send(messageFromClient.encode())

    def receiveMessage(self):
        return self.clientSocketFD.recv(1024).decode()
    
    def __del__(self):
        self.clientSocketFD.close()
