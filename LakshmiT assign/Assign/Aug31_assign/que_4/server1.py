import socket


PORT = 3004

ser = socket.socket()

ser.bind(("", PORT))

ser.listen(10)
print("Listening...")

conn, addr = ser.accept()
print(f"Connected to {addr[0]} on {addr[1]}")

while True:
    #data = conn.recv(200)
    #print(data.decode("utf-8"))
    conn.send(bytes(input(":> "),"utf-8"))

conn.close()


