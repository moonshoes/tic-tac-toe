import pygame
from settings import *

class Banner():
    def __init__(self, display, init_text, font_size):
        self.display = display
        self.text = init_text
        self.font = get_font(font_size)
        self.text_surface = self.font.render(self.text, True, FONT_COLOR)
        self.rect = pygame.Rect(
            WIDTH / 2 - self.text_surface.get_width()/2 - 5, GRID_START / 2 - self.text_surface.get_height()/2 - 5, 
            self.text_surface.get_width() + 10, self.text_surface.get_height() + 10)
    
    def print_text(self):
        text_surface = self.font.render(self.text, True, FONT_COLOR)
        self.display.blit(text_surface, 
            (WIDTH / 2 - text_surface.get_width()/2, 
            GRID_START / 2 - text_surface.get_height()/2))

    def update_text(self, text):
        pygame.draw.rect(self.display, BG_COLOR, self.rect)
        self.text = text
        self.print_text()
