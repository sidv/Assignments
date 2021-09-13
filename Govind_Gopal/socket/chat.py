import socket
import pickle
BUFFER_SIZE  = 4096
PORT = 3015
server = socket.socket()
try:
	server.bind(("",PORT))
except socket.error as e:
	print(f"Unable to bind socket {e}")

server.listen(10)
print ("Listening...")
conn,addr = server.accept()
print(f"conneced on {addr[1]}")
while True:
	data = conn.recv(BUFFER_SIZE)
	print(pickle.loads(data))
conn.close()
