"""Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
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

data = conn.recv(BUFFER_SIZE)
print(data)
data_lst = data.split(b"\n")
print("datalist")
print(data_lst)
#Convert bytes to object
actual_data = []
for i in data_lst:
	try:
		print(pickle.loads(i))
		actual_data.append(pickle.loads(i))
	except EOFError:
		print(f"Unpickling: Unable to convert to data {i}")
print(actual_data)

print(set(actual_data[0]).intersection(set(actual_data[1])))
	
#print(pickle.loads(data))
