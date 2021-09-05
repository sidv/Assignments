"""
8.Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
 
"""
import socket
import pickle

PORT =  int(input("Enter the port : "))
BUFFER_SIZE  = 300
data_lst = []
server = socket.socket()
try:
	server.bind(("",PORT))
except socket.error as e:
	print(f"Unable to bind socket {e}")

server.listen(5)
conn,addr = server.accept()
data = b''

def return_removal_lst(data_val):
	return list(set(data_val))
	
data = conn.recv(BUFFER_SIZE)
print(data)

#Convert bytes to object
data_val = pickle.loads(data)
print("*******Orginal List********")
print(data_val)
print("*******New List********")
return_new_list = return_removal_lst(data_val)
print(return_new_list)

