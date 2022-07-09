import webfilehandler, consts
from threading import Thread 

class ClientThread(Thread): 
    def __init__(self, clientFD, ip, portNumber): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = portNumber
        self.clientSocketFD = clientFD

    def run(self):
        request = self.clientSocketFD.recv(1024).decode()
        header = request.split('\n')
        filename = header[0].split()[1]
        if filename == '/':
            webFileHandlerObject = webfilehandler.WebFileHandler('./index.html')
        else:
            webFileHandlerObject = webfilehandler.WebFileHandler("." + filename)
        self.clientSocketFD.sendall(consts.httpHeader + webFileHandlerObject.readWebFile(-1))
        self.clientSocketFD.close()