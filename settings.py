import pygame

pygame.init()
pygame.font.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BG_COLOR = WHITE
FONT_COLOR = BLACK

WIDTH, HEIGHT = 600, 700

GRID_START = HEIGHT - WIDTH
GRID_BORDER = 10
CELL_SIZE = (WIDTH - 2*GRID_BORDER) // 3

def get_font(size):
        return pygame.font.SysFont("comicsans", size)