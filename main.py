import pygame, sys

pygame.init()

WIDTH = 600
HEIGHT = 600
RED = (255, 0, 0)
BG_COLOR = (30, 160, 170)


sceen =pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
sceen.fill(BG_COLOR)
#Main Game LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()