
from pysocket import PySocketServer

host = "192.168.219.110"
port = 8080

ps = PySocketServer(host, port)

def connect(client) :
    print(client.id, " connect!")
    print("addr : ", client.addr)

    client.emit("message", "helloworld")

def message(client) :
    print(client.id, "'s message : ", client.data)

def data(client) :
    print("data : ", client.data)

def disconnect(client) :
    print(client.id, "disconnect!")
    print("addr : ", client.addr)

ps.on("connect", connect)
ps.on("message", message)
ps.on("data", data)
ps.on("disconnect", disconnect)

ps.connect()
