import socket
import threading
import os
import sys
import pickle

conn_list=[]
PORT = int(input("Enter port number"))
serv = socket.socket()
BUFFER_SIZE = 200
try:
	serv.bind(("",PORT))
	print(f"Binding to {PORT}")
except socket.error:
	print("Unable to bind port")

serv.listen(10)
print("Listening")
conn, addr = serv.accept()
print(f"Connected to {addr[0]} on {addr[1]}")
i = 0
while i<30:
	data = conn.recv(10)
	data = data.decode("utf-8")
	print(data.split(":"))
	i+=1
	

conn.close()


