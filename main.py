import pygame, sys
import numpy as np
pygame.init()

BOARD_ROWS = 3
BOARD_COLS = 3 
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 25
RED = (255, 0, 0)
BG_COLOR = (30, 160, 170)
LINE_COLOR=(25, 15, 200)


screen =pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

#board
board = np.zeros((BOARD_ROWS, BOARD_COLS))
print(board)


def draw_lines():
    #1st horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    #2nd horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    #1st vertical line
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    #2nd vertical line
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

print(is_board_full())
for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
        mark_square(row, col, 1)
print(is_board_full())


draw_lines()
#Main Game LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
