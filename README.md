
# pysocket

-----

### Python Socket Module

<br/>
<br/>

    pip install py-socket-io

<br/>
<br/>

- index.py (server program)

```python
from pysocket import PySocketServer

host = "host ip"
port = "port (int)"

ps = PySocketServer(host, port)

def connect(client) :
    print(client.id, " connect!")
    print("addr : ", client.addr)

    client.emit("message", "helloworld")

def disconnect(client) :
    print(client.id, " disconnect!")
    print("addr : ", client.addr)

ps.on("connect", connect)
ps.on("disconnect", disconnect)

ps.connect()
```

<br/>
<br/>

- index2.py (client program)

```python
from pysocket import PySocketClient

host = "server host ip"
port = "server port (int)"

ps = PySocketClient(host, port)

def message(server) :
    print("server : ", server.data)

ps.on("message", message)

ps.connect()
```

<br/>

-----