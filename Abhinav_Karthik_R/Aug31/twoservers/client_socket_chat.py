import socket
import threading

client1 = socket.socket()
client2 = socket.socket()

def server1(port,server):
	client1.connect(("127.0.0.1",port))
	while True:
		data = client1.recv(200)
		print(data," ",server)

def server2(port,server):
	client2.connect(("127.0.0.1",port))
	while True:
		data = client2.recv(200)
		print(data," ",server)


t1 = threading.Thread(target=server1, args=(3003,"server1"))
t2 = threading.Thread(target=server2, args=(3004,"server2"))

t1.start()
t2.start()
t1.join()
t2.join()

client1.close()
client2.close()
