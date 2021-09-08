import socket
PORT = 3002
serv = socket.socket()
serv.bind(("",PORT))
serv.listen(10)
print("Lisening")
conn,addr = serv.accept()
print(f"Connected to {addr[0]} on {addr[1]}")
count = 0
while count < 20:
	data = conn.recv(8)
	data = data.decode("utf-8")
	print(data.split(":"))
	count +=1
	#inp = input("-:")
	#conn.send(bytes(inp,"utf-8"))
conn.close()
