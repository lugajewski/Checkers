import socket
from _thread import *
import pickle

server ="192.168.68.30"

port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")
pCount = 0


def threaded_client(conn, pCount):
    if pCount == 1:
        conn.send(str.encode(str("RED")))
    if pCount == 2:
        conn.send(str.encode(str("WHITE")))
    reply = ""
    while True:
        try:
            game = pickle.loads(conn.recv(4096))
            conn.sendall(pickle.dumps(game))
        except:
            break
    print("Lost connection")
    pCount -= 1
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    pCount += 1
    p = 0


    start_new_thread(threaded_client, (conn, pCount))