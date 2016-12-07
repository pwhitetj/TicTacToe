import sys, random, time
import strategy as ai
import pygame
from core import *
import os

#############################################################
# ttt.py
# a simple graphical tic-tac-toe client
# plays 2 strategies against each other and keeps score
# imports strategies from "strategies.py" as ai
# rest of functionality is stored in core.py
#
# This modification of mini-shell.py implements a human_gui strategy
# that responds to mouse clicks and updates a tic-tac-toe window
# It also draws the moves of any AI strategy
#
# Not much in the way of user interface exists
#
# Patrick White: December 2016
############################################################

ROUNDS = 15
if len(sys.argv)>2:
    (xpos, ypos) = sys.argv[1:3]
os.environ['SDL_VIDEO_WINDOW_POS'] = xpos+","+ypos

if sys.argv[3]=="random":
    X_STRATEGY = ai.random_strategy
else:
    X_STRATEGY = ai.minimax_strategy(10)

if sys.argv[4]=="random":
    O_STRATEGY = ai.random_strategy
else:
    O_STRATEGY = ai.minimax_strategy(10)

screen = pygame.display.set_mode((300, 300))
speed = 100
flashes = 0
quit = False

# see core.py for constants: MAX, MIN, TIE

def place(char, move):
    (x, y) = index_to_pos(move)
    if char == "X":
        color = (100, 200, 40)
    if char == "O":
        color = (100, 40, 200)
    white = (255, 255, 255)
    for count in range(3):
        pygame.draw.rect(screen, white, (x,y, 90, 90))
        pygame.display.flip()
        time.sleep(1/speed)
        pygame.draw.rect(screen, color, (x,y, 90, 90))
        pygame.display.flip()
        time.sleep(1/speed)

def show_end_screen(terminal):
    color = (255,255,255)
    if terminal == "X":
        color = (100,200,40)
    if terminal == "O":
        color = (100,40,200)
    if terminal == "TIE":
        color = (200,240,240)
    pygame.draw.rect(screen, color,(0,0,300,300))
    pygame.display.flip()
    time.sleep(0.3)

def pos_to_index(mousepos):
    col = mousepos[0] // 100
    row = mousepos[1] // 100
    index = row * 3 + col
    return index


def index_to_pos(i):
    col = i % 3
    row = i // 3
    pos = (100 * col + 5, 100 * row + 5)
    return pos


def human_gui(board, player):
    while True:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            move = pos_to_index(mousepos)
            return move
        elif event.type == pygame.QUIT:
            return None

def play(strategy_X, strategy_O, first=MAX, silent=True):
    """
    Plays strategy_X vs. strategy_O, beginning with first
    in one game. Returns X, O or TIE as a result (string)

    The functions make_move, next_player and terminal_test are
    implemented elsewhere (e.g. in core.py). The current implementation
    uses a 9-char string as the state, but that is not exposed at this level.
    """
    global quit
    board = start_state
    player = first
    current_strategy = {MAX: strategy_X, MIN: strategy_O}
    while player is not None:
        move = current_strategy[player](board, player)
        board = make_move(board, player, move)
        place(player, move)
        pygame.display.flip()
        player = next_player(board, player)
        if not silent: print_board(board)
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                player = None
                quit = True
    if quit: pygame.quit()
    show_end_screen(terminal_test(board))
    return terminal_test(board)

def start_game_gui():
    screen.fill([255, 255, 255])

    # draw lines
    pygame.draw.line(screen, (0, 0, 0), (100, 300), (100, 0))
    pygame.draw.line(screen, (0, 0, 0), (200, 300), (200, 0))
    pygame.draw.line(screen, (0, 0, 0), (300, 100), (0, 100))
    pygame.draw.line(screen, (0, 0, 0), (300, 200), (0, 200))

    pygame.display.flip()

def main():
    pygame.init()

    pygame.time.delay(1)

    for i in range(ROUNDS):
        start_game_gui()
        end = play(X_STRATEGY, O_STRATEGY, MAX)
        print("Winner:", end)
        if quit: exit()

    pygame.quit()
main()
