#6. Write code to create UDP socket to send dump file of tcpdump command to the server.

import socket
import os
client  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("127.0.0.1", 3000)

fd = open("udp_dump.txt", "wb")
fd.close()
os.system("sudo tcpdump -c 10 > udp_dump.txt")


with open("udp_dump.txt", "rb") as fd:
	while True:
		chunk = fd.read(1024)
		client.sendto(chunk, addr)
		if not chunk:
			break
client.close()
