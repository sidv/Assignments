import socket
import random
client = socket.socket()

client.connect(("127.0.0.1",3002))

while True:
	inp = random.randrange(10,100)
	client.send(bytes(str(inp),"utf-8"))
client.close()
