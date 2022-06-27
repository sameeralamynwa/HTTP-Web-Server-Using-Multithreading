import server, file 

class WebFileHandler():
    def __init__(self, path):
        self.serverObject = server.Server()
        self.path = path
        self.filePointer = open(path, 'rb')

    def readWebFile(self, buffer = 1024):
        return self.filePointer.read(buffer)