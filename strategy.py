import time
import random
import pickle
from core import *

#######################################################################
# strategy.py
#
# Contains several AI strategies for playing tic-tac-toe
#
# imports:      core.py
#
# imported by:  mini-shell.py
#
# Every strategy takes (board, player) as parameters
# and returns a move. The board/player are not changed
#
# Some strategies have wrapper functions to maintain the above signature
# This facilitates a generic shell/server script swapping strategies
######################################################################

# dictionaries for remembering boards

memory_min = {}
memory_max = {}

# MAX, MIN, TIE imported from core

def human(board, player):
    """ Asks a human for input and returns the move. No error checking. """
    move = int(input("Your move, (1-N^2)"+str(player) + ":"))-1
    return move


def random_strategy(board, player):
    """ Returns a random valid move """
    return random.choice(actions(board))


def minimax_strategy(max_depth=9):
    """ Takes a max_depth parameter and returns a new function/closure for strategy """
    def strategy(board, player):
        return minimax(board, player, max_depth)
    return strategy


def minimax(board, player, max_depth):
    """ Takes a current board and player and max_depth and returns a best move.

     This is the top level mini-max function. Note depth is ignored. We
     always search to the end of the game."""

    if player == MAX: move= max_dfs(board, player, max_depth)[1]
    if player == MIN: move= min_dfs(board, player, max_depth)[1]
    #print("player %s selects %i" % (player,move))
    return move

def min_dfs(board, player, max_depth, current_depth = 0):
    """ Recursive min-max routine. Calls Max_dfs on children.

    Returns the value of the current node (min of the children), and the
    move corresponding to that min point. In case of a tie, the "rightmost"
    child is selected. Note depth is ignored. We always search to the end
    of the game. """

    res = terminal_test(board)
    if res in endings: return evaluate[res], None
    value, move = 10**8, -1
    for m in actions(board):
        new_board, new_player = result(board, player, m)
        if (new_board, player) in memory_min:
            new_value = memory_min[new_board, player]
        else:
            new_value = max_dfs(new_board, new_player, max_depth, current_depth+1)[0]
            memory_min[new_board, player] = new_value
        value, move = min( (new_value,m),
                       (value, move) )
    return value, move


def max_dfs(board, player, max_depth, current_depth = 0):
    """ Recursive min-max routine. Calls min_dfs on children.

       Returns the value of the current node (max of the children), and the
       move corresponding to that max point. In case of a tie, the "rightmost"
       child is selected. Note depth is ignored. We always search to the end
       of the game."""

    res = terminal_test(board)
    if res in endings: return evaluate[res], None
    value, move = -10**8, -1
    for m in actions(board):
        new_board, new_player = result(board, player, m)
        if (new_board, player) in memory_max:
            new_value = memory_max[new_board, player]
        else:
            new_value = min_dfs(new_board, new_player, max_depth, current_depth + 1)[0]
            memory_max[new_board, player] = new_value
        value, move = max( (new_value,m),
                           (value, move) )
    return value, move
