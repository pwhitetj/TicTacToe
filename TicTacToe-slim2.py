import time

start_state = [0]*(9+8)
(player, other) = (1,-1)
rows = [[4*i+j for j in range(3)] for i in range(3)]
cols = [[4*j+i for j in range(3)] for i in range(3)]
diags = [list(range(0,9,4)), list(range(2,7,2))]
units = rows + cols + diags
squares = [4*i + j for i in range(3) for j in range(3)]
print("squares = ", squares)
print("units = ", units)
goals = [3,7,11,12,13,14,15,16]

count = 0
terminal_count = 0
all_boards = []


def print_board(state):
    for i in range(3):
        print(state[4*i: 4*i+3])


def terminal_test(state):
    return (not 0 in state) or goal_test(state)


def goal_test(state):
    #return any(abs(sum([evaluate[state[j]] for j in s]))==3 for s in units)
    return any(abs(state[i]==3) for i in goals)

def result(state, var):
    global other, player
    new_board = state.copy()
    new_board[var] = player
    new_board[var%4+12] += player
    new_board[var + (3-var%4)] += player
    if (var//4 == var%4): new_board[15] += player
    if (var//4 + var%4 == 2): new_board[16] += player
    player, other = other, player
    return new_board


def actions(state):
    return [i for i in squares if state[i]==0]


def dfs(state, depth):
    global count, terminal_count, all_boards

    if depth>4 and terminal_test(state):
        terminal_count+=1
        all_boards.append(state)
        return None

    for a in actions(state):
        dfs(result(state,a), depth+1)
        count+=1

state = start_state
print(actions(state))
new_player = "X"
tic = time.time()
dfs(state,0)
toc = time.time()
print("%4.2f sec. Total = %i, terminal = %i, unique = %i" % (toc-tic, count, terminal_count, 0))
