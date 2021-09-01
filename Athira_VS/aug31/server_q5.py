import socket

PORT =3002

soc = socket.socket()

soc.bind(("", PORT))
print("Binding...")

soc.listen(10)
print("Listening...")

conn, addr = soc.accept()

count = 20
res = []
while count > 0:
    data = conn.recv(8)
    #print(data)
    data = data.decode("utf-8")
    res.extend(data.split(":"))
    count -= 1

for i in res:
    print(i)
conn.close()

