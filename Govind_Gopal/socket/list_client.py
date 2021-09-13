import socket
import random
import pickle

client = socket.socket()
client.connect(("127.0.0.1",3015))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = set(a)
d = set(b)
e = list(c.intersection(d))
while True:
	client.send(pickle.dumps(e))
