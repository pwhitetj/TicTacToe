import time
import random
import pickle
import strategy as ai
from core import *

X_STRATEGY = ai.minimax_strategy(3)
O_STRATEGY = ai.random_strategy
ROUNDS = 100
start_state = "........."


def play(strategy_X, strategy_O, first = MAX, silent = True):
    board = start_state
    player = first
    current_strategy = {MAX: strategy_X, MIN: strategy_O}
    while player is not None:
        move = current_strategy[player](board, player)
        board = make_move(board, player, move)
        player = next_player(board, player)
        if not silent: print_board(board)
    return terminal_test(board)


def main():
    j=[]
    for i in range(ROUNDS):
        winner = play(X_STRATEGY, O_STRATEGY,
                      first = random.choice([MAX,MIN]),
                      silent = True)
        j.append(winner)
        print("Winner: ", winner)
    print("\nResults\n"+"%4s %4s %4s" % ("X", "O", "-"))
    print("-"*15)
    print("%4i %4i %4i" % (j.count(MAX), j.count(MIN), j.count(TIE)))


if __name__=="__main__":
    main()