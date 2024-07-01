from collections import deque  # Importing deque from the collections module
from Value import Node  # Importing the Node class from a module called Value
from Computation import Computation  # Importing the Computation class from a module called Computation
# Class representing the Breadth-First Search algorithm computation
class Breadth_First_Search(Computation):
    def __init__(self, grid):
        # Initializing Breadth-First Search algorithm with the grid
        super().__init__(grid)
    # Method to execute the Breadth-First Search algorithm
    def run_algorithm(self, snake):
        # Start with clean data structures
        self.frontier = deque([])
        self.explored_set = []
        self.path = []
        # Getting initial state and goal state for the snake
        initialstate, goalstate = self.get_initstate_and_goalstate(snake)
        # Adding initial state to the open list
        self.frontier.append(initialstate)
        # While there are states in the open list
        while len(self.frontier) > 0:
            shallowest_node = self.frontier.popleft()  # Using FIFO queue
            self.explored_set.append(shallowest_node)  # Marking the node as explored
            # Getting neighbors
            neighbors = self.get_neighbors(shallowest_node)
            # For each neighbor
            for neighbor in neighbors:
                # Checking if the path is inside the snake or outside the boundary
                if self.inside_body(snake, neighbor) or self.outside_boundary(neighbor):
                    self.explored_set.append(neighbor)  # Marking the neighbor as explored
                    continue  # Skipping this path
                # If the neighbor is neither in the frontier nor in the explored set
                if neighbor not in self.frontier and neighbor not in self.explored_set:
                    neighbor.parent = shallowest_node  # Marking parent
                    self.explored_set.append(neighbor)  # Marking the neighbor as explored
                    self.frontier.append(neighbor)  # Adding to the frontier to explore its children in the next cycle
                    # Checking if it's the goal state
                    if neighbor.equal(goalstate):
                        # Return the path
                        return self.get_path(neighbor)
        return None
