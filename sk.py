
import socket

class ServerSocket :
    def __init__(self, host, port) :
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen(self) :
        self.socket.bind((self.host, self.port))
        self.socket.listen()

    def connect(self) :
        self.client_socket, self.addr = self.socket.accept()

    # def send(self, data) :
    #     return self.socket.sendall(data) # instead of send method

    @classmethod    
    def receive(self, buffer_size, socket) :
        return socket.recv(buffer_size)

    @classmethod
    def send(self, data, socket) :
        return socket.sendall(data)

class ClientSocket(ServerSocket) :
    def connect(self) :
        self.socket.connect((self.host, self.port))

    def receive(self, buffer_size) :
        return self.socket.recv(buffer_size)

    def send(self, data) :
        return self.socket.sendall(data)