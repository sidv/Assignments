#Create multithreaded socket server which connect to multiple client.Each thread will recieve data and print on the terminal only and exit
import socket
client = socket.socket()

client.connect(("127.0.0.1",3003))

while True:
	inp = input("-:")
	client.send(bytes(inp,"utf-8"))
	data = client.recv(200)
	print(data)

client.close()
