import socket
from _thread import *
import pickle
from copy import deepcopy
from data.classes.board import Board

server ="192.168.56.1"

port = 5555
RED = (255, 0, 0)
WHITE = (255, 255, 255)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
board = Board()
board.create_board(RED)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")
pCount = 0



def threaded_client(conn, pCount):
    if pCount == 1:
        conn.send(pickle.dumps(RED))
    if pCount == 2:
        conn.send(pickle.dumps(WHITE))
    reply = ""
    while True:
        try:
            data = deepcopy(pickle.loads(conn.recv(4096)))
            if data == "get":
                conn.sendall(pickle.dumps(board.board))
                print("sending board")
            else:
                board.board = data
                print("getting board")
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