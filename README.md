
# pysocket

-----

#### Python Socket Module

<br/>

```python
from pysocket import PySocket

host = "192.168.219.110"
port = 8080

ps = PySocket(host, port)

def connect(client) :
    print(client.id, " connect!")

    client.emit("message", "helloworld")

def disconnect(client) :
    print(client.id, "disconnect!")

ps.on("connect", connect)
ps.on("disconnect", disconnect)

ps.connect()
```

<br/>

-----