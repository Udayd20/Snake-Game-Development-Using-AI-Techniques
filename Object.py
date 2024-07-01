from pygame.math import Vector2  # Importing Vector2 class from pygame.math module
from Fixed_values import BANNER_HEIGHT, NO_OF_CELLS, USER_SEED  # Importing constants from Fixed_values module
import random  # Importing random module
random.seed(USER_SEED)  # Setting the random seed for reproducibility
# Class representing an object in the game (e.g., fruit)
class Object:
    def __init__(self):
        self.position = Vector2(0, 0)  # Initializing the position of the object
        self.reset_seed()  # Resetting the random seed
    # Method to generate a new position for the fruit object
    def generate_fruit(self):
        border = NO_OF_CELLS - 1  # Define the border of the grid
        # Generate random x and y coordinates within the grid boundaries
        x = random.randrange(1, border)
        y = random.randrange(BANNER_HEIGHT, border)
        self.position = Vector2(x, y)  # Set the position of the fruit object
    # Method to reset the random seed and generate a new fruit
    def reset_seed(self):
        random.seed(USER_SEED)  # Reset the random seed
        self.generate_fruit()  # Generate a new fruit position
