
from sk import ServerSocket
from packet import Packet
import random

class Client :
    def __createSocketId(self, length=7, step=3) :
        random_hash = 0

        for _ in range(step) :
            random_hash += random.random()

        return str(random_hash).split(".")[1][:length]

    def __init__(self, socket, addr) :
        self.socket = socket
        self.addr = addr
        self.id = self.__createSocketId()
        
        self.thread = None
        self.thread_state = True # client working for thread
        self.data = None

    def emit(self, event_name, data) :
        send_packet = Packet(event_name, data)
        
        ServerSocket.send(send_packet.encode(), self.socket)

    def stop(self) :
        self.socket.close()
        self.thread_state = False
