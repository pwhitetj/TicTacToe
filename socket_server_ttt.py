### code taken from
### https://shakeelosmani.wordpress.com/2015/04/13/python-3-socket-programming-example/


import socket
import strategy as ai


def Main():
    host = "127.0.0.1"
    port = 5001

    mySocket = socket.socket()
    mySocket.bind((host, port))

    mySocket.listen(1)
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