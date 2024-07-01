from Fixed_values import NO_OF_CELLS  # Importing the constant representing the number of cells in each dimension of the grid.
class Node:
    def __init__(self, x, y):
        # Initializing a node with its coordinates (x, y) and default values for h, g, f, and parent.
        self.x = int(x)
        self.y = int(y)
        self.h = 0
        self.g = 0
        self.f = 1000000
        self.parent = None    
    def print(self):
        # Printing the coordinates of the node.
        print(f"x: {self.x} y: {self.y}")
    def equal(self, b):
        # Checking if two nodes have the same coordinates.
        return self.x == b.x and self.y == b.y
class Grid:
    def __init__(self):
        # Initializing the grid as an empty list.
        self.grid = []
        # Iterating over each row of the grid.
        for i in range(NO_OF_CELLS):
            col = []  # Initializing a list to hold the nodes of a single column.
            # Iterating over each column of the grid.
            for j in range(NO_OF_CELLS):
                # Creating a node with coordinates (i, j) and appending it to the current column.
                col.append(Node(i, j))
            # Appending the column to the grid.
            self.grid.append(col)
