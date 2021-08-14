import ProcessPooler

class PenodeClient:
    def __init__(self, clientSocket, pooler:ProcessPooler):
        self.clientSocket = clientSocket 
        self.inData = []
        self.outData = []
        self.inBuffer = '' 
        self.pooler = pooler 

    def recieveData(self):
        while True:
            data = self.clientSocket.recv(1024)
            dataList = data.split(';')
            dataList[0] = self.inBuffer + dataList[0]
            if data[-1]==';':
                self.inData.append(dataList)
                self.inBuffer = ''
            else:
                self.inData.append(dataList[:-1])
                self.inBuffer = dataList[-1]
            self.handleData()

    def handleData(self):
        while len(self.inData) != 0:   
            data = self.inData[0]      
            data = data.split()
            task = data[0]
            args = data[1:]
            self.pooler.addToPool(task,args)
            self.inData = self.inData[1:]

    