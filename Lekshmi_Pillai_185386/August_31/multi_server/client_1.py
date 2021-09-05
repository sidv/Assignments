import socket
client1 = socket.socket()
client2 = socket.socket()

client1.connect(("127.0.0.1",3002))
client2.connect(("127.0.0.1",3003))

while True:
	
	inp = input("-:")
	client1.send(bytes(inp,"utf-8"))
	data1 = client1.recv(200)
	print(data1)
	client1.close()
	
	inpu = input("-:")
	client2.send(bytes(inpu,"utf-8"))
	data2 = client2.recv(200)
	print(data2)
	client2.close()




