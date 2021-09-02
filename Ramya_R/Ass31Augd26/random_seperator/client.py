import socket
import random
import pickle

#BUFFER_SIZE = 500
client = socket.socket()
PORT = int(input("Enter port number"))
client.connect(("127.0.0.1",PORT))
i=0
while i < 30:
	inp = str(random.randint(1,30))+":"
	client.send(bytes(str(inp),"utf-8"))
	i += 1
#	data = client.recv(200)
#	print(data)

client.close()

