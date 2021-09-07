
# pysocket

-----

### Python Socket Module

<br/>

- index.py

```python
from pysocket import PySocket

host = "host ip"
port = "port in number"

ps = PySocket(host, port)

def connect(client) :
    print(client.id, " connect!")

def disconnect(client) :
    print(client.id, "disconnect!")

ps.on("connect", connect)
ps.on("disconnect", disconnect)

ps.connect()
```

<br/>

-----