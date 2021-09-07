#Create a socket application where client is sending random number continously.
#server socket

import socket
PORT = 3008
serv = socket.socket()
serv.bind(("",PORT))
serv.listen(10)
print("Lisening")
conn,addr = serv.accept()
print(f"Connected to {addr[0]} on {addr[1]}")
#count = 20
while True:
	data = conn.recv(200)
	print(data)
	#count -= 1
conn.close()
