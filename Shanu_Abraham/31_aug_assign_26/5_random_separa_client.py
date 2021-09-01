#Create a socket application where client is sending random number continously using separator.
#Client socket	
import socket
import random

client = socket.socket()

client.connect(("127.0.0.1",3004))

count = 20
while count > 0:
	data = str(random.randint(0,100))+"\n"
	client.send(bytes(str(data),"utf-8"))
	count -= 1
client.close()
