import socket
import random
client = socket.socket()

client.connect(("127.0.01",3003))

while True:
	inp = str(random.randint(2,20))
	client.send(bytes(inp,"utf-8"))
#	data = client.recv(200)
#	print(data.decode('utf-8'))
#	if inp == "bye":
#		break	 

client.close()
