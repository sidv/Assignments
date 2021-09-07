import socket

sock = socket.socket()
sock.connect(("192.168.1.8",3001))
sock.send(b"Hi I am from other pc")
data=sock.recv(100)
print(data)
sock.close()
