import socket
PORT = 3002
serv = socket.socket()
serv.bind(("",PORT))
serv.listen(10)
print("Lisening")
conn,addr = serv.accept()
print(f"Connected to {addr[0]} on {addr[1]}")
while True:
	data = conn.recv(200)
	print(data)
conn.close()
