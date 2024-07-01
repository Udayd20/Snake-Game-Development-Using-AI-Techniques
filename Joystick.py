from Snake import Snake  # Importing the Snake class from a module called Snake
from Fixed_values import NO_OF_CELLS, BANNER_HEIGHT  # Importing constants from Fixed_values module
from Value import Grid  # Importing the Grid class from a module called Value
from Depth_First_Search import Depth_First_Search  # Importing the Depth-First Search algorithm class
from Breadth_First_Search import Breadth_First_Search  # Importing the Breadth-First Search algorithm class
from Astar import Astar  # Importing the A* algorithm class
# Class representing the joystick control of the game
class Joystick:
    def __init__(self):
        # Initializing joystick attributes
        self.snake = None
        self.score = 0
        self.end = False
        self.grid = Grid().grid
        self.algo = None
        self.model_loaded = False
    # Method to reset the game state
    def reset(self):
        self.end = False
        if self.snake:
            self.snake.reset()
            self.snake = None
        self.algo = None
        self.model_loaded = False
    # Method to load a pre-trained model for the snake
    def load_model(self):
        self.snake = Snake()
        self.snake.load_model('saved_model')
        self.model_loaded = True
    # Method to get the current score of the game
    def get_score(self):
        if self.snake:
            return self.snake.score
        else:
            return 0
    # Method to handle when the snake eats a fruit
    def ate_fruit(self):
        if self.snake.ate_fruit():
            self.snake.add_body_ai()
            self.change_fruit_location()
    # Method to change the location of the fruit
    def change_fruit_location(self):
        while True:
            self.snake.create_fruit()
            position = self.snake.get_fruit()
            inside_body = False
            for body in self.snake.body:
                if position == body:
                    inside_body = True
            if not inside_body:
                break
    # Method to handle when the snake dies
    def died(self):
        current_x = self.snake.body[0].x
        current_y = self.snake.body[0].y
        if not 0 <= current_x < NO_OF_CELLS:
            self.end = True
        elif not BANNER_HEIGHT <= current_y < NO_OF_CELLS:
            self.end = True
        elif self.snake.ate_body():
            self.end = True
    # Method to get the position of the fruit
    def get_fruit_pos(self):
        return self.snake.get_fruit()
    # Method to set the path-finding algorithm for the snake
    def set_algorithm(self, algo_type):
        if self.algo is not None:
            return
        if algo_type == 'Breadth_First_Search':
            self.algo = Breadth_First_Search(self.grid)
            self.snake = Snake()
        elif algo_type == 'Depth_First_Search':
            self.algo = Depth_First_Search(self.grid)
            self.snake = Snake()
        elif algo_type == 'ASTAR':
            self.algo = Astar(self.grid)
            self.snake = Snake()
    # Method to let the AI control the snake using a specific algorithm
    def ai_play(self, algorithm):
        self.set_algorithm(algorithm)
        if self.algo is None:
            return
        pos = self.algo.run_algorithm(self.snake)
        self.update_path_finding_algo(pos)
    # Method to keep the snake moving
    def keep_moving(self):
        x = self.snake.body[0].x
        y = self.snake.body[0].y
        if self.snake.body[1].x == x:
            if self.snake.body[1].y < y:
                y = y + 1
            else:
                y = y - 1
        elif self.snake.body[1].y == y:
            if self.snake.body[1].x < x:
                x = x + 1
            else:
                x = x - 1
        return x, y
    # Method to update the path-finding algorithm's decision
    def update_path_finding_algo(self, pos):
        if pos is None:
            x, y = self.keep_moving()
        else:
            x = pos.x
            y = pos.y
        self.snake.move_ai(x, y)
        self.died()
        self.ate_fruit()
