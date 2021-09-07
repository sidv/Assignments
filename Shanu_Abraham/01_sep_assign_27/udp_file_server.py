import socket
import time

BUFFER_SIZE = 1024

ser = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ser.bind(("",3000))


time.sleep(2)
while True:
	data, addr = ser.recvfrom(BUFFER_SIZE)
	print(data.decode("utf-8"))
	if not data:
		break

ser.close() 

