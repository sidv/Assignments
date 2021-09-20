import socket

cli = socket.socket()

cli.connect(("127.0.0.1", 3000))

while True:
    cli.send(bytes(input("~<"),"utf-8"))
    data = cli.recv(200)
    print(data.decode("utf-8"))

cli.close()




