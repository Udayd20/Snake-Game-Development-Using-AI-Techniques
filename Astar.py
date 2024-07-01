from Computation import Computation  # Importing the Computation class from a module called Computation
# Class representing the A* algorithm computation
class Astar(Computation):
    def __init__(self, grid):
        # Initializing A* algorithm with the grid
        super().__init__(grid)
    # Method to execute the A* algorithm
    def run_algorithm(self, snake):
        # Clearing all data structures
        self.frontier = []
        self.explored_set = []
        self.path = []
     # Getting initial state and goal state for the snake
        initialstate, goalstate = self.get_initstate_and_goalstate(snake)
        # Adding initial state to the open list
        self.frontier.append(initialstate)
        # While there are states in the open list
        while len(self.frontier) > 0:
            # Getting node with the lowest f(n)
            lowest_index = 0
            for i in range(len(self.frontier)):
                if self.frontier[i].f < self.frontier[0].f:
                    lowest_index = i
            lowest_node = self.frontier.pop(lowest_index)
            # Checking if it's the goal state
            if lowest_node.equal(goalstate):
                return self.get_path(lowest_node)
            self.explored_set.append(lowest_node)  # Marking the node as visited
            neighbors = self.get_neighbors(lowest_node)  # Getting neighbors
            # For each neighbor
            for neighbor in neighbors:
                # Checking if the path is inside the snake, outside the boundary, or already visited
                if self.inside_body(snake, neighbor) or self.outside_boundary(neighbor) or neighbor in self.explored_set:
                    continue  # Skipping this path
                g = lowest_node.g + 1
                best = False  # Assuming neighbor path is better
                if neighbor not in self.frontier:  # First time visiting
                    neighbor.h = self.euclidean_distance(goalstate, neighbor)
                    self.frontier.append(neighbor)
                    best = True
                elif lowest_node.g < neighbor.g:  # Already visited but had a worse g, now it's better
                    best = True
                if best:
                    neighbor.parent = lowest_node
                    neighbor.g = g
                    neighbor.f = neighbor.g + neighbor.h
        return None
