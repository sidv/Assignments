import pickle
import socket
import random


BUFFER_SIZE = 300

PORT = int(input("Enter Port number: "))
client = socket.socket()
client.connect(('192.168.122.1', PORT))

# sendig random number

while True:
    num = random.randint(20, 40)
    # client.send(bytes(str(num), 'utf-8'))
    client.send(pickle.dumps(str(num) + '\n'))

    # receiving data from server
    # data = client.recv(BUFFER_SIZE)
    # print(data.decode('utf-8'))
client.close()
