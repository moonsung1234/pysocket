
from sk import Server
from event import Event
from client import Client
from packet import Packet
from threading import Thread
import time

class PySocket :
    def __clientCallback(self, client) :
        while client.thread_state :
            try :
                data = Server.receive(self.receive_size, client.socket)
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
                        client.stop()
                        self.clients.pop(i)

                time.sleep(self.delay)

            except :
                break

    def __init__(self, host, port) :
        self.server = Server(host, port)
        self.event = Event()

        # listen server
        self.server.listen()

        self.clients = []
        self.receive_size = 100000 # default receive buffer size
        self.delay = 0.5 # default delay (0.5s = 500ms)
        self.threads_state = True

        self.connect_thread = Thread(target=self.__connectCallback)
        self.connect_thread.daemon = True
        self.connect_thread.start()

        self.disconnect_thread = Thread(target=self.__disconnectCallback)
        self.disconnect_thread.daemon = True
        self.disconnect_thread.start()

    def check(self, socket) :
        try :
            Server.send(Packet("alive", "Are you alive?").encode(), socket)
        
            return True

        except :
            return False

    def on(self, event_name, callback) :
        self.event.on(event_name, callback)

    def stop(self) :
        self.server.socket.close()
        self.threads_state = False

    def connect(self) :
        # to word thread 
        while True :
            try :
                time.sleep(self.delay)

            except KeyboardInterrupt :
                self.stop()
                break