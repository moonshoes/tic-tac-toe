import pygame
from settings import *
import Game as g

pygame.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW.fill(BG_COLOR)

game = g.Game(WINDOW)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
pygame.quit()