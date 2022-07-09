import server, consts

class HTTPServer():
    def __init__(self, ip = '', portNumber = 80):
        serverObject = server.Server(ip, portNumber)
    def sendMessage(self, header, message):
        serverObject.sendMessage(consts.httpHeader + header + message)
    def receiveMessage(self):
        request = serverObject.receiveMessage()
        return request.split('\n\n')[0], request.split['\n\n'][1]
    def __del__():
        serverObject.closeClientConnection()