import socket
client = socket.socket()

client.connect(("127.0.0.1",3009))

while True:
	inp = input("-:")
	client.send(bytes(inp,"utf-8"))
	data = client.recv(200)
	print(data)

client.close()
