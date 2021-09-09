
from sk import ServerSocket, ClientSocket
from event import Event
from client import Client, Server
from packet import Packet
from threading import Thread
import time

class PySocketServer :
    def __clientCallback(self, client) :
        while client.thread_state :
            try :
                data = ServerSocket.receive(self.receive_size, client.socket)
                packet = Packet.decode(data)
                client.data = packet.data

                self.event.emit(packet.packet_name, args=[client])

            except :
                break

    def __connectCallback(self) :
        while self.threads_state :
            try :
                self.server.connect()

                client = Client(
                    self.clients,
                    self.server.client_socket,
                    self.server.addr
                )
                client.thread = Thread(target=self.__clientCallback, args=(client,))
                client.thread.daemon = True
                client.thread.start()

                self.clients.append(client)
                self.event.emit("connect", args=[client])

            except :
                break

    def __disconnectCallback(self) :
        while self.threads_state :
            try :
                for i, client in enumerate(self.clients) :
                    if not self.check(client.socket) :
                        self.event.emit("disconnect", args=[client])
                        client.close()
                        self.clients.pop(i)

                time.sleep(self.delay)

            except :
                break

    def __init__(self, host, port) :
        self.server = ServerSocket(host, port)
        self.event = Event()

        # listen server
        self.server.listen()

        self.clients = []
        self.delay = 0.3 # default delay (0.5s = 500ms)
        self.receive_size = 100000 # default receive buffer size
        self.threads_state = True

        self.connect_thread = Thread(target=self.__connectCallback)
        self.connect_thread.daemon = True
        self.connect_thread.start()

        self.disconnect_thread = Thread(target=self.__disconnectCallback)
        self.disconnect_thread.daemon = True
        self.disconnect_thread.start()

    def check(self, socket) :
        try :
            ServerSocket.send(Packet("alive", "Are you alive?").encode(), socket)
        
            return True

        except :
            return False

    def on(self, event_name, callback) :
        self.event.on(event_name, callback)

    def close(self) :
        self.server.socket.close()
        self.threads_state = False

    def connect(self) :
        # to word thread 
        while True :
            try :
                time.sleep(self.delay)

            except KeyboardInterrupt :
                self.close()
                break

class PySocketClient(PySocketServer) :
    def __setDefaultEvent(self) :
        self.event.on("alive", lambda s: s)
        # anything else may be here

    def __serverCallback(self, server) :
        self.__setDefaultEvent()

        while self.threads_state :
            try :
                data = self.client.receive(self.receive_size)
                packet = Packet.decode(data)
                server.data = packet.data

                self.event.emit(packet.packet_name, args=[server])

            except :
                break

    def __init__(self, host, port) :
        self.client = ClientSocket(host, port)
        self.event = Event()

        self.delay = 0.3 # default
        self.receive_size = 100000 # default size
        self.threads_state = True

        self.client.connect()

        self.server_thread = Thread(target=self.__serverCallback, args=[Server(self.client.socket)])
        self.server_thread.daemon = True
        self.server_thread.start()

    def close(self):
        self.client.socket.close()
        self.threads_state = False