class File:
    def File(path, mode = 'r'):
        self.path = path
        self.file = open(path, mode)

    def seek(self, position):
        self.file.seek(position)

    def tell(self):
        self.file.tell()
    
    def read(self, buffer = -1):
        return self.file.read()
    
    def write(self, toWrite):
        self.file.write(toWrite)
    
    def __del__(self):
        self.file.close()