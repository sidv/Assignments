import socket
client = socket.socket()
client2 = socket.socket()

client.connect(("192.168.122.1", 3010))
client2.connect(('192.168.122.1', 3011))

while True:
    inp = input("type message here : ")
    client.send(bytes(inp, "utf-8"))
    client2.send(bytes(inp, "utf-8"))
    data = client.recv(200)
    data2 = client2.recv(200)
    print(data.decode('utf-8'))
    print(data2.decode('utf-8'))

client.close()
client2.close()
