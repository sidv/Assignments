import socket
PORT=3006
server = socket.socket()
server.bind(("",PORT))
server.listen(10)
print("Lisening")
conn,addr = server.accept()
print(f"Connected to {addr[0]} on {addr[1]}")
count = 0
while count < 20:
	data = conn.recv(8)
	data = data.decode("utf-8")
	print(data.split(":"))
	count +=1
	
conn.close()

