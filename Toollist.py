import pygame
from Fixed_values import *  # Importing necessary constants and colors
import sys
# Defining a class to manage the menu and cursor
class Toollist:
    def __init__(self, game):
        # Initializing menu properties
        self.game = game
        self.mid_size = self.game.SIZE / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 80, 80)
        self.offset = -200
        self.title_size = 80
        self.option_size = 30
    def draw_cursor(self):
        # Drawing the cursor on the menu
        self.game.draw_text('=>', size=40, x=self.cursor_rect.x, y=self.cursor_rect.y, color=MENU_COLOR)
    def blit_menu(self):
        # Blitting the menu onto the game window
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()
# Class representing the main menu
class MainMenu(Toollist):
    def __init__(self, game):
        # Initializing main menu properties
        super().__init__(game)
        self.state = 'ASTAR'  # Initial state of the menu
        self.cursorASTAR = MENU_COLOR
        self.cursorBFS = BLACK
        self.cursorDFS = BLACK
        self.ASTARx, self.ASTARy = self.mid_size, self.mid_size - 50
        self.BFSx, self.BFSy = self.mid_size, self.mid_size
        self.DFSx, self.DFSy = self.mid_size, self.mid_size + 50
        self.cursor_rect.midtop = (self.ASTARx + self.offset, self.ASTARy)
    def change_cursor_color(self):
        # Changing cursor color based on the selected state
        self.clear_cursor_color()
        if self.state == 'ASTAR':
            self.cursorASTAR = MENU_COLOR
        elif self.state == 'Breadth_First_Search':
            self.cursorBFS = MENU_COLOR
        elif self.state == 'Depth_First_Search':
            self.cursorDFS = MENU_COLOR
    def clear_cursor_color(self):
        # Resetting all cursor colors to default
        self.cursorASTAR = BLACK
        self.cursorBFS = BLACK
        self.cursorDFS = BLACK
    def display_menu(self):
        # Displaying the main menu
        self.run_display = True
        while self.run_display:
            self.game.event_handler()
            self.check_input()
            self.game.display.fill(WINDOW_COLOR)
            self.game.draw_text('Different Paths Of Snake', size=self.title_size, x=self.game.SIZE/2, y=self.game.SIZE/2 - 2*(CELL_SIZE + NO_OF_CELLS), color=TITLE_COLOR)
            self.game.draw_text('A STAR', size=self.option_size, x=self.ASTARx, y=self.ASTARy, color=self.cursorASTAR)
            self.game.draw_text('BREADTH FIRST SEARCH', size=self.option_size, x=self.BFSx, y=self.BFSy, color=self.cursorBFS)
            self.game.draw_text('DEPTH FIRST SEARCH', size=self.option_size, x=self.DFSx, y=self.DFSy, color=self.cursorDFS)
            self.draw_cursor()
            self.change_cursor_color()
            self.blit_menu()
    def check_input(self):
        # Checking user input to navigate the menu
        self.move_cursor()
        if self.game.START:
            self.game.playing = True
            self.run_display = False   
    def move_cursor(self):
        # Handling cursor movement based on user input
        if self.game.DOWNKEY:
            if self.state == 'ASTAR':
                self.cursor_rect.midtop = (self.BFSx + self.offset, self.BFSy)
                self.state = 'Breadth_First_Search'
            elif self.state == 'Breadth_First_Search':
                self.cursor_rect.midtop = (self.DFSx + self.offset, self.DFSy)
                self.state = 'Depth_First_Search'
            elif self.state == 'Depth_First_Search':
                self.cursor_rect.midtop = (self.ASTARx + self.offset, self.ASTARy)
                self.state = 'ASTAR'
        if self.game.UPKEY:
            if self.state == 'ASTAR':
                self.cursor_rect.midtop = (self.DFSx + self.offset, self.DFSy)
                self.state = 'Depth_First_Search'
            elif self.state == 'Breadth_First_Search':
                self.cursor_rect.midtop = (self.ASTARx + self.offset, self.ASTARy)
                self.state = 'ASTAR'
            elif self.state == 'Depth_First_Search':
                self.cursor_rect.midtop = (self.BFSx + self.offset, self.BFSy)
                self.state = 'Breadth_First_Search'
