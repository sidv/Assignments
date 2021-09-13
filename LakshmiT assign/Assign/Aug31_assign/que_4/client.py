import socket
import random

cli1 = socket.socket()

cli1.connect(("127.0.0.1", 3004))

count = 0
while count < 5:
    #data = str(random.randint(0,100))+"\n"
    #cli.send(bytes(str(data),"utf-8"))
    data = cli1.recv(200)
    print(data.decode("utf-8"))
    count += 1

cli1.close()

cli2 = socket.socket()
cli2.connect(("127.0.0.1", 3005))
count = 0
while count < 5:
    #data = str(random.randint(0,100))+"\n"
    #cli.send(bytes(str(data),"utf-8"))
    data = cli2.recv(200)
    print(data.decode("utf-8"))
    count += 1

cli2.close()





