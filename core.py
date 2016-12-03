import time
import random
import pickle

N = 3
start_state = "."*(N**2)
MAX = "X"
MIN = "O"
TIE = "TIE"
endings = (MAX, MIN, TIE)
rows = [[N*i+j for j in range(N)] for i in range(N)]
cols = [[N*j+i for j in range(N)] for i in range(N)]
diags = [list(range(0,N*N,N+1)), list(range(N-1,N*N,N-2))]
units = rows + cols + diags
count = 0
terminal_count = 0
all_boards = []
evaluate = {MAX:1, MIN:-1, ".":0, TIE:0}
memory_min = {}
memory_max = {}

def print_board(board):
    for i in range(N):
        print(board[N * i: N * i + N])
    print()


def terminal_test(board):
    win = winner(board)
    if win is not None: return win
    if not "." in board: return TIE
    else: return False


def goal_test(board):
    return any(abs(sum([evaluate[board[j]] for j in s])) == N for s in units)

def winner(board):
    if any(sum([evaluate[board[j]] for j in s]) == N for s in units):
        return MAX
    if any(sum([evaluate[board[j]] for j in s]) == -N for s in units):
        return MIN
    return None

def result(board, player, var):
    assert board[var] == ".", "%s is not empty" % str(var)
    new_board = board[:var] + player + board[var + 1:]
    return new_board, toggle(player)

def make_move(board, player, move):
    assert board[move] == ".", "%s is not empty" % str(move)
    new_board = board[:move] + player + board[move + 1:]
    return new_board

def next_player(board, player):
    if terminal_test(board):
        return None
    else:
        return toggle(player)

def actions(board):
    open_squares = [i for (i,c) in enumerate(board) if c == "."]
    random.shuffle(open_squares)
    #if len(open_squares)==9:
    #    return [0,1,4]
    #else:
    return open_squares


def toggle(player):
    if player==MAX:
        return MIN
    else:
        return MAX


def dfs(board, player, depth):
    global count, terminal_count, all_boards

    if depth>4 and terminal_test(board):
        terminal_count+=1
        all_boards.append(board)
        return None

    for a in actions(board):
        dfs(*result(board, player, a), depth + 1)
        count+=1