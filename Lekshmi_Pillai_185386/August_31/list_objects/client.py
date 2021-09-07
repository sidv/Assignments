import socket
import pickle

PORT = int(input("Enter the port :"))
client = socket.socket()
client.connect(("127.0.0.1",PORT))


#send list
lst = [1, 1, 2, 3, 5, 8, 13, 21,34, 55]
lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
client.send(pickle.dumps(lst))
client.send(b"\n")
client.send(pickle.dumps(lst1))
client.close()
