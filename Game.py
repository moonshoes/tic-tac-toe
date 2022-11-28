import pygame
from pygame.locals import *
from settings import *

pygame.font.init()

class Game():
    def __init__(self, display):
        self.display = display
        self.turn_x = True
        self.grid = []
        self.has_won = False
        self.empty_grid()

    def empty_grid(self):
        self.grid = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
    
    def reset_game(self):
        self.empty_grid()
        self.turn_x = True
        self.has_won = False
    
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
        self.winning_condition()
        if not self.has_won:
            self.change_turn()
        
    
    def winning_condition(self):
        result = self.check_top_left()
        if not result:
            result = self.check_bottom_right()
        if not result:
            result = self.check_center()
        self.has_won = result
    
    def check_top_left(self):
        result = False
        topleft = self.grid[0][0]
        
        if not self.cell_empty(0,0):
            if topleft == self.grid[0][1]:
                result = topleft == self.grid[0][2]
            if not result and topleft == self.grid[1][1]:
                result = topleft == self.grid[2][2]
            if not result and topleft == self.grid[1][0]:
                result = topleft == self.grid[2][0]

        return result

    def check_bottom_right(self):
        result = False
        bottomright = self.grid[2][2]

        if not self.cell_empty(2,2):
            if bottomright == self.grid[0][2]:
                result = bottomright == self.grid [1][2]
            if not result and bottomright == self.grid[2][0]:
                result = bottomright == self.grid[2][1]

        return result

    def check_center(self):
        result = False
        center = self.grid[1][1]

        if not self.cell_empty(1,1):
            if center == self.grid[0][1]:
                result = center == self.grid[2][1]
            if not result and center == self.grid[1][0]:
                result = center == self.grid[1][2]
            if not result and center == self.grid[0][2]:
                result = center == self.grid[2][0]

        return result