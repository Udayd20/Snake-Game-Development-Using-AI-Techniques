import pygame  # Importing the pygame module
from Fixed_values import *  # Importing constants from Fixed_values module
from Toollist import *  # Importing classes from Toollist module
from Joystick import Joystick  # Importing Joystick class from Joystick module
import sys  # Importing sys module
# Class representing the player interface
class Player_Interface:
    def __init__(self):
        pygame.init()  # Initializing pygame
        # Setting up game clock and screen update event
        self.clock = pygame.time.Clock()
        self.SCREEN_UPDATE = pygame.USEREVENT
        self.speed_up = 80 
        # Setting initial game speed
        self.speed = 110
        pygame.time.set_timer(self.SCREEN_UPDATE, self.speed)
        # Initializing joystick controller
        self.controller = Joystick()
        # Setting up game state variables
        self.running, self.playing = True, False
        self.UPKEY, self.DOWNKEY, self.START, self.BACK = False, False, False, False
        # Setting up display window
        self.SIZE = CELL_SIZE * NO_OF_CELLS
        self.display = pygame.Surface((self.SIZE, self.SIZE))
        self.window = pygame.display.set_mode((self.SIZE, self.SIZE))
        # Setting up font
        self.font_name = 'Arial'
        # Setting up main menu
        self.main_menu = MainMenu(self) 
        self.curr_menu = self.main_menu
    # Method to handle the game loop
    def game_loop(self):
        while self.playing:
            self.event_handler()
            if self.BACK:
                self.playing = False
            self.display.fill(WINDOW_COLOR)
            if self.controller.algo is not None:
                self.draw_elements()
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.clock.tick(60)
            self.reset_keys()
    # Method to draw game elements on the screen
    def draw_elements(self):
        self.draw_banner()
        self.draw_game_stats()
        fruit = self.controller.get_fruit_pos()
        snake = self.controller.snake
        self.draw_fruit(fruit)
        self.draw_snake(snake)
        self.draw_score()
        if not self.controller.model_loaded and self.view_path:
            self.draw_path()
    # Method to draw game statistics
    def draw_game_stats(self):
        instruction = 'Use W to quicken, Q to backpedal'
        self.draw_text(instruction, size=20, x=self.SIZE/2, y=(CELL_SIZE * NO_OF_CELLS) - NO_OF_CELLS, color=BLACK)
        self.draw_text(self.curr_menu.state, size=30, x=self.SIZE/2, y=CELL_SIZE)
    # Method to draw the path of the algorithm
    def draw_path(self):
        for path in self.controller.algo.path:
            x = int(path.x * CELL_SIZE)
            y = int(path.y * CELL_SIZE)
            path_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            shape_surf = pygame.Surface(path_rect.size, pygame.SRCALPHA)
            pygame.draw.rect(shape_surf, PATHCOLOR, shape_surf.get_rect())
            pygame.draw.rect(self.display, BANNER_COLOR, path_rect, 1)
            self.display.blit(shape_surf, path_rect)
    # Method to draw the snake
    def draw_snake(self, snake):
        self.draw_snake_head(snake)
        for body in snake.body[1:]:
            self.draw_snake_body(body)
    # Method to draw the snake head
    def draw_snake_head(self, snake):
        self.draw_rect(snake.body[0], color=SNAKE_HEAD_COLOR)
    # Method to draw the snake body
    def draw_snake_body(self, body):
        self.draw_rect(body, color=SNAKE_COLOR, border=True)
    # Method to draw a rectangle
    def draw_rect(self, element, color, border=False):
        x = int(element.x * CELL_SIZE)
        y = int(element.y * CELL_SIZE)
        body_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.display, color, body_rect)
        if border:
            pygame.draw.rect(self.display, WINDOW_COLOR, body_rect, 3)
    # Method to draw the fruit
    def draw_fruit(self, fruit):
        x = int(fruit.x * CELL_SIZE)
        y = int(fruit.y * CELL_SIZE)
        fruit_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.display, FRUIT_COLOR, fruit_rect)
    # Method to draw the banner
    def draw_banner(self):
        banner = pygame.Rect(0, 0, self.SIZE, BANNER_HEIGHT * CELL_SIZE)
        pygame.draw.rect(self.display, BANNER_COLOR, banner)
    # Method to draw the score
    def draw_score(self):
        score_text = 'Points: ' + str(self.controller.get_score())
        score_x = self.SIZE - (CELL_SIZE + 2*len(score_text))
        score_y = CELL_SIZE
        self.draw_text(score_text, 20, score_x, score_y, WINDOW_COLOR)
    # Method to display game over screen
    def game_over(self):
        self.display.fill(MENU_COLOR)
        high_score = f'Peak Score {self.controller.get_score()}'
        to_continue = 'Hit Enter to Go On'
        self.draw_text(high_score, size=35, x=self.SIZE/2, y=self.SIZE/2)
        self.draw_text(to_continue, size=30, x=self.SIZE/2, y=self.SIZE/2 + 2*CELL_SIZE, color=BLACK)
        self.window.blit(self.display, (0, 0))
        pygame.display.update()
        self.wait_for_input()
        self.controller.reset()
    # Method to wait for user input
    def wait_for_input(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
                    if event.key == pygame.K_s:
                        self.controller.save_model()
                        waiting = False
                if self.is_quit(event):
                    pygame.quit()
                    sys.exit()
    # Method to check if quit event occurred
    def is_quit(self, event):
        if event.type == pygame.QUIT:
            self.running, self.playing = False, False
            return True
        return False
    # Method to handle events
    def event_handler(self):
        for event in pygame.event.get():
            if self.is_quit(event):
                pygame.quit()
                sys.exit()
            elif self.playing and event.type == pygame.USEREVENT:
                self.controller.ai_play(self.curr_menu.state) 
                if self.controller.end:  
                    self.playing = False
                    self.game_over()  
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START = True
                    self.view_path = False
                elif event.key == pygame.K_q:
                    self.BACK = True
                    self.controller.reset()
                elif event.key == pygame.K_SPACE:
                    self.view_path = not self.view_path
                elif event.key == pygame.K_DOWN:
                    self.DOWNKEY = True
                elif event.key == pygame.K_UP:
                    self.UPKEY = True
                elif event.key == pygame.K_w:
                    self.speed_up = -1 * self.speed_up
                    self.speed = self.speed + self.speed_up
                    pygame.time.set_timer(self.SCREEN_UPDATE, self.speed)
    # Method to reset key flags
    def reset_keys(self):
        self.UPKEY, self.DOWNKEY, self.START, self.BACK = False, False, False, False
    # Method to draw text on the screen
    def draw_text(self, text, size, x, y, color=WINDOW_COLOR):
        font = pygame.font.SysFont(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
# Starting point of the program
if __name__ == "__main__":
    game_gui = Player_Interface()
    game_gui.game_loop()
