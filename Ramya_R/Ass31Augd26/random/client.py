import socket
import random

client = socket.socket()

client.connect(("127.0.0.1",3007))

while True:
	inp = str(random.randint(1,30))
	client.send(bytes(inp,"utf-8"))

client.close()
