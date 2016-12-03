from copy import deepcopy, copy

rows = [[3*i+j for j in range(3)] for i in range(3)]
cols = [[3*j+i for j in range(3)] for i in range(3)]
diags = [list(range(0,9,4)), list(range(2,7,2))]

class TTTBoard:
    def __init__(self, state = None, next = None):
        if state==None:
            state = [""]*9
        if next is None:
            next = "X"
        self.state = state
        self.next = next
        self.actions = [idx for (idx,val) in enumerate(self.state) if val == ""]
        self.rowScore = [0]*3
        self.colScore = [0]*3
        self.diagScore = [0]*2

    def goal_test(self):
        return(any(abs(s)==3 for s in self.rowScore+self.colScore+self.diagScore))

    def assign(self, var, val):
        assert(self.state[var]=="")
        assert(isinstance(val, str))
        assert(val == self.next)
        self.state[var] = val
        row = var // 3
        col = var % 3
        diag = -1
        if (row-col==0): diag = 0
        if (row+col==2): diag = 1
        if val=="X":
            score = 1
            self.next = "O"
        else:
            score = -1
            self.next = "X"
        self.rowScore[row]+= score
        self.colScore[col] += score
        if diag > -1: self.diagScore[diag] += score
        self.actions.remove(var)

    def player(self):
        return self.next

    def utility(self):
        if any(s ==  3 for s in self.rowScore+self.colScore+self.diagScore): return 1
        if any(s == -3 for s in self.rowScore+self.colScore+self.diagScore): return -1
        return 0

    def result(self, a):
        B = deepcopy(self)
        B.assign(a, B.next)
        return B

    def __str__(self):
        s=""
        for i in range(3):
            for j in range(3):
                c = self.state[3*i+j]
                if c=="": c = "."
                s += c
            s += "\n"
        return s

def minimax_decision(state: TTTBoard):
    L= list((min_value(state.result(a),1),a) for a in state.actions)
    print(L)
    c=max(L)
    return(c[1])
    #return max((a for a in state.actions), key=lambda x:min_value(state.result(x), 1))

def min_value(state: TTTBoard, depth):
    #print("MIN", depth, state.utility(), state)
    if state.goal_test(): return state.utility()
    if len(state.actions)==0: return 0
    v = 10000000
    for a in state.actions:
        v = min(v, max_value(state.result(a), depth+1))
    #print("MIN", depth, state, "returns", v)
    return v

def max_value(state: TTTBoard, depth):
    #print("MAX", depth, state.utility(), state)
    if state.goal_test(): return state.utility()
    if len(state.actions)==0: return 0
    v = -10000000
    for a in state.actions:
        v = max(v, min_value(state.result(a), depth+1))
    #print("MAX", depth, state, "returns", v)
    return v

def test():
    T = TTTBoard()
    print(T)
    print(T.actions)
    for j in range(9):
        B = deepcopy(T)
        var = minimax_decision(B)
        print("%s goes to %i" % (T.next, var))
        T.assign(var, T.next)
        print(T, T.rowScore, T.colScore, T.diagScore)

test()