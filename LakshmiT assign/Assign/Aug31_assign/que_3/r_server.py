import socket

PORT =3006

soc = socket.socket()

soc.bind(("", PORT))
print("BInding")

soc.listen(10)

conn, addr = soc.accept()

while True:
    data = conn.recv(8)
    print(data.decode("utf-8"))

conn.close()

