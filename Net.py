import numpy as np  # Importing numpy library with alias np
import math  # Importing math module
from Computation import Computation  # Importing the Computation class from a module called Computation
from Fixed_values import USER_SEED  # Importing USER_SEED constant from Fixed_values module
np.random.seed(USER_SEED)  # Setting the random seed for reproducibility
# Sigmoid activation function
def sigmoid(m):
    return 1/(1+np.exp(-m))
# Rectified Linear Unit (ReLU) activation function
def ReLU(x):
    return x * (x > 0)
# Hyperbolic Tangent (tanh) activation function
def tanh(x):
    return np.tanh(x)
# Class representing a Neural Network
class NeuralNework:
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes  # Number of input nodes
        self.hidden_nodes = hidden_nodes  # Number of hidden nodes
        self.output_nodes = output_nodes  # Number of output nodes
        self.shape = (input_nodes, hidden_nodes, output_nodes)  # Shape of the network
        self.initialize()  # Initialize the network
    # Method to initialize the weights and biases of the network
    def initialize(self):
        # Initialize biases with random values
        self.biases = [np.random.randn(i)
                       for i in [self.hidden_nodes, self.output_nodes]]
        # Initialize weights with random values
        self.weights = [np.random.randn(j, i)
                        for i, j in zip([self.input_nodes, self.hidden_nodes], [self.hidden_nodes, self.output_nodes])]
    # Method for feedforward propagation through the network
    def feedforward(self, input_matrix):
        input_matrix = np.array(input_matrix)  # Convert input to numpy array
        # Iterate through each layer and compute the output
        for b, w in zip(self.biases, self.weights):
            input_matrix = tanh(np.dot(w, input_matrix)+b)  # Apply tanh activation function
        return input_matrix
    # Method for crossover operation between two networks
    def crossover(self, networkA, networkB):
        weightsA = networkA.weights.copy()  # Copy weights from network A
        weightsB = networkB.weights.copy()  # Copy weights from network B
        biasesA = networkA.biases.copy()  # Copy biases from network A
        biasesB = networkB.biases.copy()  # Copy biases from network B
        # Perform crossover for weights
        for i in range(len(self.weights)):
            length = len(self.weights[i])
            split = np.random.uniform(0, 1, size=length)
            split = np.random.randint(1, length)
            self.weights[i] = weightsA[i].copy()
            self.weights[i][split > 0.5] = weightsB[i][split > 0.5].copy()
        # Perform crossover for biases
        for i in range(len(self.biases)):
            length = len(self.biases[i])
            split = np.random.randint(1, length)
            self.biases[i] = biasesA[i].copy()
            self.biases[i][:split] = biasesB[i][:split].copy()
    # Method for mutation operation
    def mutation(self, a, val):
        if np.random.rand() < val:  # Check if mutation probability is met
            return np.random.randn()  # Generate random mutation value
        return a
    # Method to apply mutation to the network
    def mutate(self, val):
        muation = np.vectorize(self.mutation)  # Vectorize mutation function
        # Apply mutation to weights
        for i in range(len(self.weights)):
            self.weights[i] = muation(self.weights[i], val)
        # Apply mutation to biases
        for i in range(len(self.biases)):
            self.biases[i] = muation(self.biases[i], val)
    # Method to print the shape, weights, and biases of the network
    def print(self):
        print('shape', self.shape)
        print('weights', self.weights)
        print('biases', self.biases)
