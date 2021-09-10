
from .sk import ServerSocket
from .packet import Packet
import random

class Client :
    def __createSocketId(self, length=7, step=3) :
        random_hash = 0

        for _ in range(step) :
            random_hash += random.random()

        return str(random_hash).split(".")[1][:length]

    def __init__(self, clients, socket, addr) :
        self.clients = clients
        self.socket = socket
        self.addr = addr
        self.id = self.__createSocketId()
        
        self.thread = None
        self.thread_state = True # client working for thread
        self.data = None

    def emit(self, event_name, data, id=None) :
        send_packet = Packet(event_name, data)
        
        if not id == None :
            for client in self.clients :
                if client.id == id :
                    ServerSocket.send(send_packet.encode(), client.socket)

                    break

        else :
            ServerSocket.send(send_packet.encode(), self.socket)

    def emitall(self, event_name, data) :
        for client in self.clients :
            self.emit(event_name, data, id=client.id)

    def close(self) :
        self.socket.close()
        self.thread_state = False

class Server(Client) :
    def __init__(self, socket) :
        self.socket = socket
        self.data = None

    def close(self) :
        self.socket.close()

    def emit(self, event_name, data) :
        send_packet = Packet(event_name, data)
        
        ServerSocket.send(send_packet.encode(), self.socket)