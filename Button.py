import pygame
from settings import *

class Button():
    def __init__(self, display, font_size):
        self.screen = display
        self.text = "reset"
        self.font = get_font(font_size)
        self.text_surface = self.font.render(self.text, 1, FONT_COLOR)
    
        self.text_length = self.text_surface.get_width()
        self.text_height = self.text_surface.get_height()
        self.padding_x = 10
        self.padding_y = 3
        self.margin = 10
        self.x = WIDTH - self.text_length - 2*self.padding_x - self.margin
        self.y = GRID_START - self.text_height - 2*self.padding_y - self.margin
        self.width = self.text_length + 2*self.padding_x
        self.height = self.text_height + 2*self.padding_y

    def draw(self):
        pygame.draw.rect(self.screen, BLACK, (self.x, self.y, self.width, self.height), 2)
        self.screen.blit(self.text_surface, 
            (self.x + self.width/2 - self.text_length/2, self.y + self.height/2 - self.text_height/2))

    def clicked(self, pos):
        x, y =  pos
       
        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False
        
        return True