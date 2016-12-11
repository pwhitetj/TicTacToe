#!/usr/bin/python3
### code taken from
### https://shakeelosmani.wordpress.com/2015/04/13/python-3-socket-programming-example/


import socket
import strategy as ai
import sys

def Main():
    host = socket.gethostname()
    port = 5001

    if (sys.argv[1]!=""):
        port = int(sys.argv[1])

    mySocket = socket.socket()
    mySocket.bind((host, port))

    mySocket.listen(5)
    conn, addr = mySocket.accept()
    print("Connection from: " + str(addr))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected  user: " + str(data))
        (board, player) = data.split()
        move = ai.minimax(board, player, 100)
        data = str(move)
        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    Main()
