import socket
import random
client = socket.socket()

client.connect(("127.0.0.1",3001))

while True:
	inp = str(random.randint(1,20))+"\n"
	client.send(bytes(inp,"utf-8"))
	
	
client.close()
