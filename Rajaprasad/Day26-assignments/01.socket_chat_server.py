import socket
# chat application

PORT = 3000

server = socket.socket()

server.bind(("", PORT))
server.listen(10)
print('Server listening .......')
conn, address = server.accept()
print(f'connected to {address[0]} on {address[1]}')
while True:
    data = conn.recv(200)
    print(data.decode('utf-8'))
    inp = input("Type message here : ")
    conn.send(bytes(inp, 'utf-8'))
conn.close()
