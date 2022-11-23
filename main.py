import pygame
from settings import *
import Game as g

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW.fill(BG_COLOR)

game = g.Game(WINDOW)

def draw_grid():
        h_line_1 = ((GRID_BORDER, GRID_START + GRID_BORDER + CELL_SIZE), 
            (WIDTH - GRID_BORDER, GRID_START + GRID_BORDER + CELL_SIZE))
        h_line_2 = ((GRID_BORDER, GRID_START + GRID_BORDER + 2*CELL_SIZE), 
            (WIDTH - GRID_BORDER, GRID_START + GRID_BORDER + 2*CELL_SIZE))

        v_line_1 = ((GRID_BORDER + CELL_SIZE, GRID_START + GRID_BORDER), 
            (GRID_BORDER + CELL_SIZE, HEIGHT - GRID_BORDER))
        v_line_2 = ((GRID_BORDER + 2*CELL_SIZE, GRID_START + GRID_BORDER), 
            (GRID_BORDER + 2*CELL_SIZE, HEIGHT - GRID_BORDER))

        pygame.draw.line(WINDOW, BLACK, h_line_1[0], h_line_1[1], 2)
        pygame.draw.line(WINDOW, BLACK, h_line_2[0], h_line_2[1], 2)

        pygame.draw.line(WINDOW, BLACK, v_line_1[0], v_line_1[1], 2)
        pygame.draw.line(WINDOW, BLACK, v_line_2[0], v_line_2[1], 2)

def mouse_in_grid(pos):
    x, y = pos
    if y >= GRID_START + GRID_BORDER and x >= GRID_BORDER or x <= WIDTH - GRID_BORDER:
        return True
    else:
        return False

def get_row_col(pos):
    x, y = pos

    row = (y - GRID_START - GRID_BORDER) // CELL_SIZE
    col = (x - GRID_BORDER) // CELL_SIZE

    return row, col

def place_move(row, col):
    game.place_move(row, col)
    # 


running = True
draw_grid()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if pygame.mouse.get_pressed():
            pos = pygame.mouse.get_pos()

    
    pygame.display.update()
pygame.quit()