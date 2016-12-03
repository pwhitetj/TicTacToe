import pygame, sys, random, time

#pygame.init()
screen = pygame.display.set_mode((300, 300))
screen.fill([255, 255, 255])

state = [0] * 9

# draw lines
pygame.draw.line(screen, (0, 0, 0), (100, 300), (100, 0))
pygame.draw.line(screen, (0, 0, 0), (200, 300), (200, 0))
pygame.draw.line(screen, (0, 0, 0), (300, 100), (0, 100))
pygame.draw.line(screen, (0, 0, 0), (300, 200), (0, 200))

pygame.display.flip()
pygame.time.delay(500)


def place(char, mousepos):
    global state
    col = mousepos[0] // 100
    row = mousepos[1] // 100
    index = row * 3 + col
    box_upper_left = (row * 100, col * 100)
    if char == "X":
        state[index] = 1
        color = (100, 200, 40)
    if char == "O":
        state[index] = -1
        color = (100, 40, 200)
    white = (255, 255, 255)
    for count in range(3):
        pygame.draw.rect(screen, white, (col * 100 + 5, row * 100 + 5, 90, 90))
        pygame.display.flip()
        time.sleep(0.1)
        pygame.draw.rect(screen, color, (col * 100 + 5, row * 100 + 5, 90, 90))
        pygame.display.flip()
        time.sleep(0.1)


def get_move():
    global state
    l = [i for (i, j) in enumerate(state) if j == 0]
    random.shuffle(l)
    assert len(l) > 0, "No moves left"
    return l.pop()


def toggle(char):
    if char == "X":
        return "O"
    if char == "O":
        return "X"
    return "X"


def pos_to_index(mousepos):
    col = mousepos[0] // 100
    row = mousepos[1] // 100
    index = row * 3 + col


def index_to_pos(i):
    col = i % 3
    row = i // 3
    pos = (100 * col + 5, 100 * row + 5)
    return pos


char = "X"
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            char = toggle(char)
            print("Human: ", pos_to_index(mousepos))
            place(char, mousepos)
            pygame.display.flip()

            time.sleep(1)
            char = toggle(char)
            computer = get_move()
            place(char, index_to_pos(computer))
            print("computer ", computer, "state", state)
            pygame.display.flip()
        if event.type == pygame.QUIT:
            pygame.quit()
