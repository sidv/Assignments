import socket
import random

cli = socket.socket()

cli.connect(("127.0.0.1", 3002))

while True:
    data = str(random.randint(0,100))+"\n"
    cli.send(bytes(str(data),"utf-8"))
    #data = cli.recv(200)
    #print(data.decode("utf-8"))

cli.close()




