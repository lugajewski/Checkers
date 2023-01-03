import socket
from _thread import *

server = "192.168.68.30"
port = 5555

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serv.bind((server, port))
except socket.error as e:
    str(e)

serv.listen(2)
print("Waiting for connection, server started")

def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved: ", reply)
                print("Sending: ", reply)
            conn.sendall(str.encode((reply)))
        except:
            break
    print("Lost connection")

while True:
    conn, addr = serv.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))
