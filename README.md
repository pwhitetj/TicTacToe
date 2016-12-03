# TicTacToe

A simple client-server model Tic Tac Toe game. The client is mini-shell.py and the server is strategy.py. 
Both import core.py for shared functionality. In the client you can select minimax, human or random as strategies
and set the number of games to play. The main routine plays the games and shows the result. A correct
minimax will never lose.

The underlying data type is a string for the board, e.g. "........." or "X..O..XOX". Only the server
knows the datatype. The client doesn't care, except that winners are either MIN, MAX or TIE, which are 
constants defined in core.py

The current core.py is a bit sub-optimal in the way it deals with terminal states, but it's not a big deal.

The current minmax routine keeps a dictonary of seen boards which really speeds up games after the first search.
server.py (now defunct) saves this dictionary as a pickle file.

Also tested with 4x4 tic tac toe. After an initial search (15 min), it plays very fast.

ttt.py implements a very simply point-and-click GUI.

Written by Patrick White, Dec 2016

