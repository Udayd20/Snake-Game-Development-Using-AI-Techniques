from pygame.math import Vector2  # Importing the Vector2 class from the pygame.math module
from Object import Object  # Importing the Object class from a module called Object
from Net import NeuralNework  # Importing the NeuralNework class from a module called Net
import pickle  # Importing the pickle module for object serialization
# Class representing the snake
class Snake:
    def __init__(self, hidden=8):
        # Initializing the snake with default body and fruit positions, and other attributes
        self.body = [Vector2(5, 8), Vector2(4, 8), Vector2(3, 8)]
        self.fruit = Object()
        self.score = 0
        self.fitness = 0
        self.life_time = 0
        self.steps = 0
        self.hidden = hidden
        self.network = NeuralNework(5, self.hidden, 3)
    # Method to save the neural network model to a file
    def save_model(self, network, name):
        with open(name, "wb") as file:
            pickle.dump(network, file)
    # Method to load the neural network model from a file
    def load_model(self, name):
        with open(name, 'rb') as file:
            self.network = pickle.load(file)
    # Method to reset the snake's attributes
    def reset(self):
        self.body = [Vector2(5, 8), Vector2(4, 8), Vector2(3, 8)]
        self.fruit.reset_seed()
        self.score = 0
        self.fitness = 0
        self.steps = 0
        self.network = NeuralNework(5, self.hidden, 3)
    # Getter method for the x-coordinate of the snake's head
    def get_x(self):
        return self.body[0].x
    # Getter method for the y-coordinate of the snake's head
    def get_y(self):
        return self.body[0].y
    # Getter method for the position of the fruit
    def get_fruit(self):
        return self.fruit.position
    # Method to check if the snake has eaten the fruit
    def ate_fruit(self):
        if self.fruit.position == self.body[0]:
            self.score += 1
            self.life_time -= 40
            return True
        return False
    # Method to generate a new fruit
    def create_fruit(self):
        self.fruit.generate_fruit()
    # Method to move the snake according to AI
    def move_ai(self, x, y):
        self.life_time += 1
        self.steps += 1
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
        self.body[0].x = x
        self.body[0].y = y
    # Method to add a body segment to the snake
    def add_body_ai(self):
        last_indx = len(self.body) - 1
        tail = self.body[-1]
        before_last = self.body[-2]
        if tail.x == before_last.x:
            if tail.y < before_last.y:
                self.body.append(Vector2(tail.x, tail.y-1))
            else:
                self.body.append(Vector2(tail.x, tail.y+1))
        elif tail.y == before_last.y:
            if tail.x < before_last.x:
                self.body.append(Vector2(tail.x - 1, tail.y))
            else:
                self.body.append(Vector2(tail.x + 1, tail.y))
    # Method to check if the snake has collided with itself
    def ate_body(self):
        for body in self.body[1:]:
            if self.body[0] == body:
                return True
        return False
