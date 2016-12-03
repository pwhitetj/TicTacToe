import time
import random
import pickle
from strategy import *



def play(strategy_X, strategy_O, first = MAX, verbosity = 1):
    board = start_state
    player = first
    current_strategy = {MAX: strategy_X, MIN: strategy_O}
    if verbosity > 3: print(board)
    while  terminal_test(board) not in endings:
        board, player = current_strategy[player](board, player)
        if verbosity > 3: print_board(board)
    if verbosity > 2: print("Winner:", terminal_test(board))
    if verbosity > 2: print_board(board)
    if verbosity == 1: print(board, "winner:", terminal_test(board))
    return terminal_test(board)

def main():
#    data = open("TicTacToe-Boards-16.pk", "rb")
#    memory_min, memory_max = pickle.load(data)
    j=[]
    tic = time.time()
    for i in range(3):
        j += [play(minimax_strategy(3), random_strategy, first = random.choice([MAX,MIN]), verbosity=5)]
        #print("*", j)
    toc = time.time()
    print(j.count(MAX), j.count(MIN), j.count(TIE))
    #print(j)
    print("%4.2f seconds"% (toc-tic))
    print(len(memory_max) + len(memory_min), "boards loaded")

    out = open("TicTacToe-Boards-"+str(N)+".pk", "wb")
    pickle.dump((memory_min, memory_max), out)


if __name__=="__main__":
    main()