import socket


PORT = 3004
serv = socket.socket()

serv.bind(("",PORT))
serv.listen(10)
print("Listening")
conn,addr = serv.accept()
print(f"Connected to {addr[0]} on {addr[1]}")
while True:
	# data = conn.recv(200)
	# print(data)
	inp = input("Enter data to client -:")
	conn.send(bytes(inp,"utf-8"))
	
conn.close()	
