import socket
import random
client = socket.socket()
client2 = socket.socket()
client.connect(("127.0.0.1",3010))
client2.connect(("127.0.0.1",3011))

while True:
	inp1 = input("1. -:")
	client.send(bytes(inp1,"utf-8"))
	inp2 = input("2. -:")
	client2.send(bytes(inp2,"utf-8"))
	data1 = client.recv(200)
	print(data1.decode('utf-8'))
	data2 = client2.recv(200)
	print(data2.decode('utf-8'))
	if inp1 == "bye" or inp2 == "bye":
		break	 
	

client.close()
client2.close()

