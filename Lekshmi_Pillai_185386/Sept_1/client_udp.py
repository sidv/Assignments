import socket
import os


client  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("127.0.0.1", 3005)

fd = open("log.txt", "wb")
os.system("sudo tcpdump -c 30 > log.txt")
fd.close()

with open("log.txt", "rb") as fd:
	while True:
		chunk = fd.read(4096)
		client.sendto(chunk, addr)
		if not chunk:
			break
client.close()
