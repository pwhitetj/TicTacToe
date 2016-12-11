import pickle
import strategy as myAI
import core
import random
import importlib
import os
import fnmatch
import re

#############################################################
# mini-shell.py
# a simple tic-tac-toe client
# plays 2 strategies against each other and keeps score
# imports strategies from "strategies.py" as ai
# rest of functionality is stored in core.py
#
# Patrick White: December 2016
############################################################

SILENT = False

# see core.py for constants: MAX, MIN, TIE

def play(strategy_X, strategy_O, first=core.MAX, silent=True):
    """
    Plays strategy_X vs. strategy_O, beginning with first
    in one game. Returns X, O or TIE as a result (string)

    The functions make_move, next_player and terminal_test are
    implemented elsewhere (e.g. in core.py). The current implementation
    uses a 9-char string as the state, but that is not exposed at this level.
    """
    board = core.start_state
    player = first
    current_strategy = {core.MAX: strategy_X, core.MIN: strategy_O}
    while player is not None:
        move = current_strategy[player](board, player)
        board = core.make_move(board, player, move)
        player = core.next_player(board, player)
        if not silent: core.print_board(board)
    return core.terminal_test(board)


def main(strat_lib, rounds):
    """
    Plays ROUNDS tic-tac-toe games and keeps a count of
    wins/ties. Uses strategies defined as global constants above.
    Selects a random starting player
    """

    ai = importlib.import_module("students."+strat_lib)

    X_STRATEGY = ai.minimax_strategy(9)
    O_STRATEGY = myAI.random_strategy

    j = []
    for i in range(rounds):
        try:
            game_result = play(X_STRATEGY, O_STRATEGY,
                          first=random.choice([core.MAX, core.MIN]),
                          silent=SILENT)
            j.append(game_result)
            #print("Winner: ", game_result)
        except core.IllegalMoveError as e:
            print(e)
            j.append("FORFEIT")
    #print("\nResults\n" + "%4s %4s %4s" % ("X", "O", "-"))
    #print("-" * 15)
    print("%4i %4i %4i" % (j.count(core.MAX), j.count(core.MIN), j.count(core.TIE)))
    (w,l,t) = (j.count(core.MAX), j.count(core.MIN), j.count(core.TIE))
    return [(w,l,t),(w+t)/(w+l+t)]

def error_check():
    outfile = open("errors.txt", "w")
    prefix = "students"
    index = open("students-index.txt","r")
    for line in index.readlines():
        (block, name, file, newfile) = line.strip().split(";")
        strat_lib = newfile.replace(".py","")
        try:
            value = main(strat_lib, 1)
            print(block, strat_lib, "OK")
            print("%s\t%s\t%s" % (block, strat_lib, "OK"), file=outfile)

        except BaseException as e:
            print ("%s\t%s\t%s\t%s\t%s" % (block, strat_lib, "ERROR", e.__class__, e))
            print("%s\t%s\t%s\t%s\t%s" % (block, strat_lib, "ERROR", e.__class__, e), file=outfile)

    index.close()
    outfile.close()

def get_results():
    outfile = open("results.txt", "w")
    prefix = "students"
    index = open("students-index.txt","r")
    for line in index.readlines():
        (block, name, file, newfile) = line.strip().split(";")
        strat_lib = newfile.replace(".py","")
        try:
            [(w,l,t),score] = main(strat_lib, 20)
            print("%s\t%s\t%i\t%i\t%i\t%f" % (block, strat_lib, w, l, t, score ))
            print("%s\t%s\t%i\t%i\t%i\t%f" % (block, strat_lib, w, l, t, score ), file=outfile)

        except BaseException as e:
            print ("%s\t%s\t%s\t%s\t%s" % (block, strat_lib, "ERROR", e.__class__, e))
            print("%s\t%s\t%s\t%s\t%s" % (block, strat_lib, "ERROR", e.__class__, e), file=outfile)

    index.close()
    outfile.close()

if __name__ == "__main__":
    get_results()
