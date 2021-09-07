
import socket
from packet import Packet

host = "192.168.219.110"
port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


while True :
    try :
        data = client.recv(102400)
        packet = Packet.decode(data)

        if packet.packet_name == "message" :
            print(packet.data)

    except KeyboardInterrupt :
        break