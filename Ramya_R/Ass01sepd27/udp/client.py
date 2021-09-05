import socket
import os


sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("127.0.0.1", 3002)

fd = open("udpdump.txt", "wb")
fd.close()
os.system("sudo tcpdump -c 10 > udpdump.txt")


with open("udpdump.txt", "rb") as fd:
	while True:
		chunk = fd.read(1024)
		sock.sendto(chunk, addr)
		if not chunk:
			break
sock.close()
