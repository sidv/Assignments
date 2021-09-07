import socket
import os
cli  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("127.0.0.1", 3000)
fd = open("tcp_dump_log.txt", "wb")
fd.close()
os.system("sudo tcpdump -c 10 > tcp_dump_log.txt")

with open("tcp_dump_log.txt", "rb") as fd:
	while True:
		chunk = fd.read(1024)
		cli.sendto(chunk, addr)
		if not chunk:
			break
cli.close()
