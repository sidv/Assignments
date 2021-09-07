import socket

PORT = 3001 #port number on which my socket will interact with application layer

sock = socket.socket() #Creating socket /creating socket object

sock.bind(('',PORT))
print(f"Connecting on {PORT}")

sock.listen(50) #listening to other socket
print("Listening")

conn,addr = sock.accept()	#Accepting connection/established connection returns two values connection object,address
print(f"Esatablished conection with {addr}")
data=conn.recv(100)
print(data)

conn.send(b"Hi! This is sid") #sending data

conn.close()
print("Connection closed")


