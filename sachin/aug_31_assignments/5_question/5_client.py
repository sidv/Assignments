import socket
import random
client = socket.socket()
client.connect(("127.0.0.1",3002))
count = 0
while count < 20:
    data = str(random.randint(0,100))+":"
    client.send(bytes(str(data),"utf-8"))
    count += 1

client.close()
  