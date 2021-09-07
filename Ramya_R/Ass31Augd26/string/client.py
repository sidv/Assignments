import socket
import random

client = socket.socket()
client1 = socket.socket()

client.connect(("127.0.0.1",3006))
client1.connect(("127.0.0.1",3007))
while True:
	inp = input("-:")
	client.send(bytes(inp,"utf-8"))
	inp1 = input("-:")
	client1.send(bytes(inp,"utf-8"))
	data = client.recv(200)
	print(data)
	data1 = client1.recv(200)
	print(data1)

client.close()
client1.close()
