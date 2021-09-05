import socket
import time

BUFFER_SIZE = 2000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("", 3000))


time.sleep(2)
while True:
    data, addr = server.recvfrom(BUFFER_SIZE)
    print(data.decode("utf-8"))
    if not data:
        break

server.close()
