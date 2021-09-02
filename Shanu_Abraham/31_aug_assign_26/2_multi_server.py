#Create multithreaded socket server which connect to multiple client.
#Each thread will recieve data and print on the terminal only and exit

#multithreading

import socket
import threading

conn_list = []
PORT = 3003
serv = socket.socket()

try:
	serv.bind(("",PORT))
	print(f"Binding to {PORT}")
except socket.error:
	print("Unable to bind port")

serv.listen(5)
print("Listening")

def server_client_connection(conn,addr,loc):
	print(f"Connected to {addr[0]} on {addr[1]}")
	while True:
		if conn_list[loc] is None:
			break
		data = conn.recv(200)
		print(f"{addr[0]}:>{data.decode('utf-8')}")
	conn.send((bytes(input(f"{addr[0]}-:<"),"utf-8")))

count = 1
while True:
	conn,addr = serv.accept()
	print(conn)
	print(addr)
	th = threading.Thread(target = server_client_connection,args=(conn,addr,len(conn_list)))
	conn_list.append((conn,addr,th))
	th.start()
	count+=1
	if count > 2:
		break

for i in conn_list:
	tmp = i
	tmp[0].close()
	i=None
	tmp[2].join()
	print(f"{tmp[1]} connection closed")

