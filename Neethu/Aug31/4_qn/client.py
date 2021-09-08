#Client socket	
import socket

client = socket.socket()
client.connect(("127.0.0.1",3006))


count = 0
while count < 5:
	data = client.recv(200)
	print(data.decode("utf-8"))
	count+=1
client.close()


client2 = socket.socket()
client2.connect(("127.0.0.1",3007))

count = 0
while count < 5:
	data1 = client.recv(200)
	print(data1.decode("utf-8"))
	count+=1
client2.close()
	



