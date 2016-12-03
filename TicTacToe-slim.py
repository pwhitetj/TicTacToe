import time
import random
import pickle

start_state = "........."
MAX = "X"
MIN = "O"
TIE = "TIE"
endings = (MAX, MIN, TIE)
player = MAX
other = MIN
rows = [[3*i+j for j in range(3)] for i in range(3)]
cols = [[3*j+i for j in range(3)] for i in range(3)]
diags = [list(range(0,9,4)), list(range(2,7,2))]
units = rows + cols + diags
count = 0
terminal_count = 0
all_boards = []
evaluate = {MAX:1, MIN:-1, ".":0, TIE:0}
memory_min = {}
memory_max = {}

def print_board(board):
    for i in range(3):
        print(board[3 * i: 3 * i + 3])
    print()

def terminal_test(board):
    win = winner(board)
    if win is not None: return win
    if not "." in board: return TIE
    else: return False


def goal_test(board):
    return any(abs(sum([evaluate[board[j]] for j in s])) == 3 for s in units)

def winner(board):
    if any(sum([evaluate[board[j]] for j in s]) == 3 for s in units):
        return MAX
    if any(sum([evaluate[board[j]] for j in s]) == -3 for s in units):
        return MIN
    return None

def result(board, player, var):
    assert board[var] == ".", "%s is not empty" % str(var)
    new_board = board[:var] + player + board[var + 1:]
    return new_board, toggle(player)


def actions(board):
    open_squares = [i for (i,c) in enumerate(board) if c == "."]
    random.shuffle(open_squares)
    if len(open_squares)==9:
        return [0,1,4]
    else:
        return open_squares


def dfs(board, player, depth):
    global count, terminal_count, all_boards

    if depth>4 and terminal_test(board):
        terminal_count+=1
        all_boards.append(board)
        return None

    for a in actions(board):
        dfs(*result(board, player, a), depth + 1)
        count+=1

def toggle(player):
    if player==MAX:
        return MIN
    else:
        return MAX


def human(board, player):
    move = int(input("Your move, (1-9)"+str(player) + ":"))-1
    board, player = result(board, player, move)
    return board, player


def random_strategy(board, player):
    return result(board, player, random.choice(actions(board)))


def minimax_strategy(max_depth):
    def strategy(board, player):
        return minimax(board, player, max_depth)
    return strategy


def minimax(board, player, max_depth):
    if player == MAX: move= max_dfs(board, player, max_depth)[1]
    if player == MIN: move= min_dfs(board, player, max_depth)[1]
    #print("player %s selects %i" % (player,move))
    return result(board, player, move)


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

def dfs_walk():
    board = start_state
    print(actions(board))
    player = "O"
    tic = time.time()
    dfs(board, player,0)
    toc = time.time()
    print("%4.2f sec. Total = %i, terminal = %i, unique = %i" % (toc-tic, count, terminal_count, len(set(all_boards))))

if __name__=="__main__":
    data = open("TicTacToe-Boards.pk", "rb")
    memory_min, memory_max = pickle.load(data)
    j=[]
    tic = time.time()
    for i in range(10000):
        j += [play(minimax_strategy(3), random_strategy, first = random.choice([MAX,MIN]), verbosity=0)]
        #print("*", j)
    toc = time.time()
    print(j.count(MAX), j.count(MIN), j.count(TIE))
    #print(j)
    print("%4.2f seconds"% (toc-tic))
    print(len(memory_max) + len(memory_min), "boards loaded")

#out = open("TicTacToe-Boards.pk", "wb")
#pickle.dump((memory_min, memory_max), out)
