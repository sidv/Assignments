import socket
import time

BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(("",3002))


time.sleep(2)
while True:
	data, addr = sock.recvfrom(BUFFER_SIZE)
	print(data.decode("utf-8"))
	if not data:
		break

sock.close()
