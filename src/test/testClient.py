import sys

sys.path.insert(1, '../')

import client

class TestClient:
    def __init__(self):
        pass

    def testConnection(self):
        clientObject = client.Client()
        clientObject.connectToServer()
        messageFromServer = clientObject.receiveMessage()
        if messageFromServer == 'Thanks for connecting':
            print('Test Connection Passed')
        else:
            print('Test Connection Failed')
        clientObject.sendMessage()
        

if __name__ == '__main__':
    testObject = TestClient()
    testObject.testConnection()