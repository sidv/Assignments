import socket
#Chat app

PORT = 3002
serv = socket.socket() #Creating soccket

serv.bind(("",PORT))
serv.listen(10)
print("Listening")
conn,addr = serv.accept()
print(f"Connected to {addr[0]}")
while True:
	data = conn.recv(2)
	print(data)
	
conn.close()	
