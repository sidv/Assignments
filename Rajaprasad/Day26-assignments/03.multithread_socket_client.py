import socket
import random
client = socket.socket()

client.connect(("192.168.122.1", 3003))

while True:
    inp = str(random.randint(20, 40))
    client.send(bytes(inp, "utf-8"))
    data = client.recv(200)
    print(data.decode('utf-8'))

client.close()
