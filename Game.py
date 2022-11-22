import pygame
from pygame.locals import *
from settings import *

class Game():
    def __init__(self, display):
        self.display = display
        self.draw_grid()
    
    def draw_grid(self):
        h_line_1 = ((GRID_BORDER, GRID_START + GRID_BORDER + CELL_SIZE), 
            (WIDTH - GRID_BORDER, GRID_START + GRID_BORDER + CELL_SIZE))
        h_line_2 = ((GRID_BORDER, GRID_START + GRID_BORDER + 2*CELL_SIZE), 
            (WIDTH - GRID_BORDER, GRID_START + GRID_BORDER + 2*CELL_SIZE))

        v_line_1 = ((GRID_BORDER + CELL_SIZE, GRID_START + GRID_BORDER), 
            (GRID_BORDER + CELL_SIZE, HEIGHT - GRID_BORDER))
        v_line_2 = ((GRID_BORDER + 2*CELL_SIZE, GRID_START + GRID_BORDER), 
            (GRID_BORDER + 2*CELL_SIZE, HEIGHT - GRID_BORDER))

        pygame.draw.line(self.display, BLACK, h_line_1[0], h_line_1[1], 2)
        pygame.draw.line(self.display, BLACK, h_line_2[0], h_line_2[1], 2)

        pygame.draw.line(self.display, BLACK, v_line_1[0], v_line_1[1], 2)
        pygame.draw.line(self.display, BLACK, v_line_2[0], v_line_2[1], 2)