import socket
import pickle
import random
PORT = int(input("Enter the port :"))
client = socket.socket()
client.connect(("127.0.0.1",PORT))


#send list
lst = [1,2,2,5,4,8,4,9,5,4]
client.send(pickle.dumps(lst))
client.close()
