
from pysocket import PySocketClient

host = "192.168.219.110"
port = 8080

ps = PySocketClient(host, port)

def message(server) :
    print("server : ", server.data)

ps.on("message", message)

ps.connect()