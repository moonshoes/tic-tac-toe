import pygame
from pygame.locals import *
from settings import *

pygame.font.init()

class Game():
    def __init__(self, display):
        self.display = display
        self.turn_x = True
        self.grid = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def change_turn(self):
        self.turn_x = not self.turn_x

    def turn_icon(self):
        if self.turn_x:
            return "X"
        else:
            return "O"
    
    def cell_empty(self, row, col):
        return self.grid[row][col] == ""
    
    def place_move(self, row, col):
        self.grid[row][col] = self.turn_icon()
        self.change_turn()