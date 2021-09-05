import socket
import pickle
import random
PORT = int(input("Enter the port :"))
client = socket.socket()
client.connect(("127.0.0.1",PORT))


#send list
random_num = random.randint(1,9)
print(random_num)
num = int(input("Guess your number : "))
client.send(pickle.dumps(random_num))
client.send(b"\n")
client.send(num.to_bytes(2,'little'))
client.close()
