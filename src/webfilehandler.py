class WebFileHandler():
    def __init__(self, path):
        self.path = path
        self.filePointer = open(path, 'rb')

    def readWebFile(self, buffer = 1024):
        return self.filePointer.read(buffer)
    
    def seek(self, setPosition):
        self.filePointer.seek(setPosition)
