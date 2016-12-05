from core import *
import importlib

#############################################################
# tournament.py
# a simple tic-tac-toe tournament manager
# loads all the strategies in strategies/*.py
# plays round robin.
#
# plays 2 strategies against each other and keeps score
# imports strategies from "strategies.py" as ai
# rest of functionality is stored in core.py
#
# Patrick White: December 2016
############################################################

ROUNDS = 1000

# see core.py for constants: MAX, MIN, TIE

def play(strategy_X, strategy_O, first=MAX, silent=True):
    """
    Plays strategy_X vs. strategy_O, beginning with first
    in one game. Returns X, O or TIE as a result (string)

    The functions make_move, next_player and terminal_test are
    implemented elsewhere (e.g. in core.py). The current implementation
    uses a 9-char string as the state, but that is not exposed at this level.
    """
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
    """
    Plays ROUNDS tic-tac-toe games and keeps a count of
    wins/ties. Uses strategies defined as global constants above.
    Selects a random starting player
    """

    record = {}
    for i in range(100, 110):
        for j in range(100, 110):
            ai_1 = importlib.import_module("strategies.student_ai_"+str(i))
            ai_2 = importlib.import_module("strategies.student_ai_"+str(j))
            results = []
            for g in range(20):
                game_result = play(ai_1.minimax_strategy(), ai_2.minimax_strategy(),
                              first=random.choice([MAX, MIN]),
                              silent=True)
                results.append(game_result)
            tally = (results.count(MAX), results.count(MIN), results.count(TIE))
            #print("Results: %i vs %i: [%i, %i, %i]" % (i, j, *tally))

            # score = Wins - Losses + 0.5Ties
            record[i,j] = tally[0]-tally[1]+0.5*tally[2]

    for i in range(100, 110):
        print(i, ":", end="")
        for j in range(100, 110):
            print("%4i" % record[i,j], end="")
        print()


if __name__ == "__main__":
    main()
