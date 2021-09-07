"""
7.Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
 
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

#Convert bytes to object
data_val = pickle.loads(data_lst[0])
guess_val = int.from_bytes(data_lst[1],'little')

#comparison
if data_val == guess_val :
	print("Exactly right")
elif data_val < guess_val :
	print("Too High")
else:
	print("Too Low")
