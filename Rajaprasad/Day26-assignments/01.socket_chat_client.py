import socket

client = socket.socket()
# 127.0.0.1 -- > server ip address
# 3000  -- > server port
client.connect(("192.168.122.1", 3000))

while True:
    inp = input("type message here : ")
    client.send(bytes(inp, "utf-8"))
    data = client.recv(200)
    print(data.decode('utf-8'))

client.close()
