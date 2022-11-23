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
        self.change_turn = not self.change_turn

    def turn_icon(self):
        if self.turn_x:
            return "X"
        else:
            return "O"
    
    def place_move(self, row, col):
        self.grid[row][col] = self.turn_icon()
        self.change_turn()