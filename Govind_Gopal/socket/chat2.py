import socket

PORT = 3011
serv1 = socket.socket()

serv1.bind(('',PORT))
serv1.listen(10)
print ("Listening...")
while True:
	conn,addr = serv1.accept()
	print(f"Connected to {addr[0]} on {addr[1]}")
	data = conn.recv(200)
	print(data.decode("utf-8"))
	inp = input("-:")
	conn.send(bytes(inp,"utf-8"))
	if inp == "bye":
		break
conn.close()
