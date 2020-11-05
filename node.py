
'''
This class is for the individual nodes in the network, as well as the weights that connect them.

Please forgive the long variable naming convention, but as this is my first time making a neural net with
user defined parameters (except for the number of hidden layers), I need the clarity.
'''

from numpy import random

class Node:

  def __init__(self, number_of_nodes_in_next_layer):

    ### VARIABLES ###
    self.weights = [] # the weights coming out of the node. 0th weight connects to 0th node in next layer, etc.
    self.value = 0 # the value of the node

    ### WEIGHTS ###
    # give this node a different weight for every node in the next layer
    for index in range(number_of_nodes_in_next_layer):
      self.weights.append(random.randn()) # a random number between -3 and 3, which tends to be good for weights