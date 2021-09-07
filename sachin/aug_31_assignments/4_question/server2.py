#server2 socket

import socket
PORT = 3007
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
