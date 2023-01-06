import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.68.30"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
        print(self.p)

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            side = pickle.loads(self.client.recv(2048))
            return side
        except:
            pass

    def send_board(self, data):
        try:
            self.client.send(pickle.dumps(data))
        except socket.error as e:
            print(e)

    def get_board(self):
        try:
            self.client.send(pickle.dumps("get"))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)
