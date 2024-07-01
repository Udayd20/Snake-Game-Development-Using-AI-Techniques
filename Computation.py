from abc import ABC, abstractmethod  # Importing ABC and abstractmethod from the abc module
from Fixed_values import NO_OF_CELLS, BANNER_HEIGHT  # Importing constants from Fixed_values module
from Value import Node  # Importing the Node class from a module called Value
import math  # Importing the math module
# Abstract base class representing the computation process
class Computation(ABC):
    def __init__(self, grid):
        # Initializing computation with the grid and data structures
        self.grid = grid
        self.frontier = []
        self.explored_set = []
        self.path = []
    # Method to get initial and goal states for the snake
    def get_initstate_and_goalstate(self, snake):
        return Node(snake.get_x(), snake.get_y()), Node(snake.get_fruit().x, snake.get_fruit().y)
    # Method to calculate Manhattan distance between two nodes
    def manhattan_distance(self, nodeA, nodeB):
        distance_1 = abs(nodeA.x - nodeB.x)
        distance_2 = abs(nodeA.y - nodeB.y)
        return distance_1 + distance_2
    # Method to calculate Euclidean distance between two nodes
    def euclidean_distance(self, nodeA, nodeB):
        distance_1 = nodeA.x - nodeB.x
        distance_2 = nodeA.y - nodeB.y
        return math.sqrt(distance_1**2 + distance_2**2)
    # Abstract method to run the computation algorithm
    @abstractmethod
    def run_algorithm(self, snake):
        pass
    # Method to retrieve the path from a node to the root
    def get_path(self, node):
        if node.parent == None:
            return node
        while node.parent.parent != None:
            self.path.append(node)
            node = node.parent
        return node
    # Method to check if a node is inside the snake's body
    def inside_body(self, snake, node):
        for body in snake.body:
            if body.x == node.x and body.y == node.y:
                return True
        return False
    # Method to check if a node is outside the grid boundary
    def outside_boundary(self, node):
        if not 0 <= node.x < NO_OF_CELLS:
            return True
        elif not BANNER_HEIGHT <= node.y < NO_OF_CELLS:
            return True
        return False
    # Method to retrieve neighboring nodes of a given node
    def get_neighbors(self, node):
        i = int(node.x)
        j = int(node.y)
        neighbors = []
        # Left neighbor [i-1, j]
        if i > 0:
            neighbors.append(self.grid[i-1][j])
        # Right neighbor [i+1, j]
        if i < NO_OF_CELLS - 1:
            neighbors.append(self.grid[i+1][j])
        # Top neighbor [i, j-1]
        if j > 0:
            neighbors.append(self.grid[i][j-1])
        # Bottom neighbor [i, j+1]
        if j < NO_OF_CELLS - 1:
            neighbors.append(self.grid[i][j+1])
        return neighbors
