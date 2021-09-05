import socket
import threading

conn_list = []

PORT = 3001

ser = socket.socket()
ser.bind(("", PORT))
print("Binding to Port...")

ser.listen(10)
print("Listening")

def client_server_conn(conn, addr, conn_list_len):
    print(f"Connected to {addr[0]} on {addr[1]}")
    while True:
        if conn_list[conn_list_len] == None:
            break
        data = conn.recv(200)
        print(f"{addr[0]}:> {data.decode('utf-8')}")
        conn.send(bytes(input(f":>>"), "utf-8"))


count = 1
while True:
    conn, addr = ser.accept()
    th = threading.Thread(target = client_server_conn, args = (conn, addr, len(conn_list)))
    conn_list.append((conn,addr,th))
    th.start()
    count += 1
    if count > 2:
        break

for tup in conn_list:
    x = tup
    x = None
    tup[0].close()
    tup[2].join()
    print(f"tup[1] connection closed")



