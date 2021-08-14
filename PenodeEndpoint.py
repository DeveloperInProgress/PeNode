import socket, ssl

class PenodeEndpoint:
    def __init__(self):
        self.ws = socket.create_server(('127.0.0.1',24))
        self.openConns = {}

    def listenForConnections(self):
        self.ws.listen(1)
        conn, addr = self.ws.accept()
        self.connectClient(self,addr)
        self.listenForConnections()

    def connectClient(self,addr):
        if not authenticate:
            conn.close()
        else:
            self.openConns[addr] = conn 

    def disconnectClient(self,addr):
        if addr in self.openConns:
            openConns[addr].close()
            del openConns[addr]

    def authenticate(self,addr):
        return True

    def sendData(self,addr,data):
        if addr in self.openConns:
            self.openConns[addr].send(data) 

    def recvData(self,addr):
        while True:
            data = self.openConns[addr].recv(1024)
            