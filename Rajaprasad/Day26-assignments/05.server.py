import socket
import pickle

PORT = int(input("Enter the port : "))
BUFFER_SIZE = 300

server = socket.socket()
try:
    server.bind(("", PORT))
except socket.error as e:
    print(f"Unable to bind socket {e}")
server.listen(5)
conn, addr = server.accept()
data = b''


while True:  # For large data use this method
    chunk = conn.recv(BUFFER_SIZE)  # Read fix amount of chunk
    data += chunk  # Append bytes to the data
    # if len of chunk is less than buffer size its last part of data then break
    if len(chunk) < BUFFER_SIZE:
        break

# data = data.decode('utf-8')
data = pickle.loads(data)
print(data)
conn.close()
