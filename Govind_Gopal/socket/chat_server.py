import socket
import threading

conn_list=[]
PORT = 3003
serv = socket.socket()
try:
	serv.bind(('',PORT))
	print(f"Connecting on {PORT}")
except socket.error:
	print("Unable to connect to port")
	
serv.listen(50)
print("Listening...")

def server_client_connection(conn,addr,loc):
	print(f"Connected to {addr[0]} on {addr[1]}")
	while True:
		if conn_list[loc] is None:
			break
		data = conn.recv(2)
		print(f"{addr[0]}:>{int(data.decode('utf-8'))}")
#		inp = input(f"{addr[0]}-:")
#		conn.send(bytes(inp,"utf-8"))
			

while True:
	conn,addr = serv.accept()
	th = threading.Thread(target = server_client_connection, args = (conn,addr,len(conn_list)))
	conn_list.append((conn,addr,th))
	th.start()

for i  in conn_list:
	tmp = i
	tmp[0].close()
	i=None    
	tmp[2].join()
	print(f"{tmp[1]} connection closed")
	
		

