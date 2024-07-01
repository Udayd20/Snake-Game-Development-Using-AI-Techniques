from Value import Node  # Importing the Node class from a module called Value
from Computation import Computation  # Importing the Computation class from a module called Computation
# Class representing the Depth-First Search algorithm computation
class Depth_First_Search(Computation):
    def __init__(self, grid):
        # Initializing Depth-First Search algorithm with the grid
        super().__init__(grid)
    # Recursive method to perform Depth-First Search
    def recursive_DFS(self, snake, goalstate, currentstate):
        # Check if current state is the goal state
        if currentstate.equal(goalstate):
            return self.get_path(currentstate)
        # If already visited, return None
        if currentstate in self.explored_set:
            return None
        self.explored_set.append(currentstate)  # Mark current state as visited
        neighbors = self.get_neighbors(currentstate)  # Get neighbors
        # For each neighbor
        for neighbor in neighbors:
            # Check if neighbor is not inside snake, outside boundary, and not already visited
            if not self.inside_body(snake, neighbor) and not self.outside_boundary(neighbor) and neighbor not in self.explored_set:
                neighbor.parent = currentstate  # Mark parent node
                path = self.recursive_DFS(
                    snake, goalstate, neighbor)  # Recursively check neighbor
                if path != None:
                    return path  # Found path
        return None
    # Method to run the Depth-First Search algorithm
    def run_algorithm(self, snake):
        # To avoid looping in the same location
        if len(self.path) != 0:
            # While there is a path, keep going
            path = self.path.pop()
            if self.inside_body(snake, path):
                self.path = []  # Reset path if inside body
            else:
                return path
        # Start with clean data structures
        self.frontier = []
        self.explored_set = []
        self.path = []
        initialstate, goalstate = self.get_initstate_and_goalstate(snake)
        self.frontier.append(initialstate)
        # Return path
        return self.recursive_DFS(snake, goalstate, initialstate)
