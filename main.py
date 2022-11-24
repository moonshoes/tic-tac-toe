import pygame
from settings import *
import Game as g

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW.fill(BG_COLOR)

game = g.Game(WINDOW)
banner_text = "X's turn"
banner_font = get_font(50)
banner_surface = pygame.surface.Surface((WIDTH, GRID_START))
banner_rect = banner_surface.get_rect(topleft=(0,0))

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
    if (y >= GRID_START + GRID_BORDER and y <= HEIGHT - GRID_BORDER and
         x >= GRID_BORDER and x <= WIDTH - GRID_BORDER):
        return True
    else:
        return False

def get_row_col(pos):
    x, y = pos

    row = (y - GRID_START - GRID_BORDER) // CELL_SIZE
    col = (x - GRID_BORDER) // CELL_SIZE

    return row, col

def get_cell_center(row, col):
    x = GRID_BORDER + col * CELL_SIZE + 0.5 * CELL_SIZE
    y = GRID_START + GRID_BORDER + row * CELL_SIZE + 0.5 * CELL_SIZE
    return x, y

def place_move(row, col):
    font = get_font(CELL_SIZE)
    text_surface = font.render(game.turn_icon(), True, BLACK)
    cell_x, cell_y = get_cell_center(row, col)
    WINDOW.blit(text_surface, 
        (cell_x - text_surface.get_width()/2, cell_y - text_surface.get_height()/2))

    # Move placed in actual grid last because this also changes the turn automatically!
    game.place_move(row, col)
    text = "{}'s turn".format(game.turn_icon())
    print_banner_text(text)

def print_banner_text(text):
    banner_surface.fill(BG_COLOR)
    text_surface = banner_font.render(text, True, BLACK)
    WINDOW.blit(text_surface, 
        (WIDTH / 2 - text_surface.get_width()/2, GRID_START / 2 - text_surface.get_height()/2))


running = True
draw_grid()
print_banner_text(banner_text)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if mouse_in_grid(pos):
                row, col = get_row_col(pos)
                if game.cell_empty(row, col):
                    place_move(row, col)

    
    pygame.display.update()
pygame.quit()