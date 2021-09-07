#Create a socket application where client is sending random number continously.
#Client socket	
import socket
import random

client = socket.socket()

client.connect(("127.0.0.1",3008))

#count = 20
while True:
	data = str(random.randint(0,100))
	client.send(bytes(str(data),"utf-8"))
	#count -= 1
client.close()
