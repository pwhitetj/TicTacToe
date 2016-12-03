import time
import random
import pickle
from core import *

def human(board, player):
    move = int(input("Your move, (1-N^2)"+str(player) + ":"))-1
    board, player = result(board, player, move)
    return board, player


def random_strategy(board, player):
    return random.choice(actions(board))


def minimax_strategy(max_depth=9):
    def strategy(board, player):
        return minimax(board, player, max_depth)
    return strategy


def minimax(board, player, max_depth):
    if player == MAX: move= max_dfs(board, player, max_depth)[1]
    if player == MIN: move= min_dfs(board, player, max_depth)[1]
    #print("player %s selects %i" % (player,move))
    return move

def min_dfs(board, player, max_depth, current_depth = 0):
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
