### code taken from
### https://shakeelosmani.wordpress.com/2015/04/13/python-3-socket-programming-example/

import socket
from core import *

host = '127.0.0.1'
port = 5001
silent = False

mySocket = socket.socket()
mySocket.connect((host, port))


def human(board, player):
    """ Asks a human for input and returns the move. No error checking. """
    move = int(input("Your move, (1-9)"+str(player) + ":"))-1
    return move

def ai_server(board, player):
    message = "%s %s" % (board, player)
    mySocket.send(message.encode())
    data = mySocket.recv(1024).decode()
    move = int(data)
    print("-----------sent %s rcvd %s" % (message, data))
    return move

def Main():
    board = start_state
    player = MAX

    strategy_X = ai_server
    strategy_O = ai_server

    current_strategy = {MAX: strategy_X, MIN: strategy_O}
    print_board(board)

    while player is not None:
        move = current_strategy[player](board, player)
        board = make_move(board, player, move)
        player = next_player(board, player)
        if not silent: print_board(board)
    return terminal_test(board)

    mySocket.close()


if __name__ == '__main__':
    Main()