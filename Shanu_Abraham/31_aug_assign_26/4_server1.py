#Create a socket application where a client connect to two servers and fetch string from the server.

#server1 socket

import socket
PORT = 3008
serv = socket.socket()
serv.bind(("",PORT))

serv.listen(10)
print("Lisening")

conn,addr = serv.accept()
print(conn)
print(addr)
print(f"Connected to {addr[0]} on {addr[1]}")
while True:
	#data = conn.recv(200)
	#print(data)
#	inp = input("-:")
	conn.send(bytes(input(":>"),"utf-8"))
conn.close()
