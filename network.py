
'''
This class is for a neural network of nodes. The weights and nodes are contained in the node class in node.py. The
biases and the feedforward process are handled in this file.

Please forgive the long variable naming convention, but as this is my first time making a neural net with
user defined parameters (except for the number of hidden layers), I need the clarity.
'''

from node import *
from numpy import random
from numpy import square
from geometry import *

class Network:

  def __init__(self, input_layer_size, hidden_layer_size, output_layer_size):

    # console output
    print("An AI has been randomly generated.")
    
    ### VARIABLES ###

    self.input_nodes = [] # an array that holds all the input nodes
    self.hidden_nodes = [] # an array that holds all the hidden layer nodes
    self.output_nodes = [] # an array that holds all the output layer nodes
    self.hidden_bias = random.randn() # a random number between -3 and 3, tends to be good for biases
    self.output_bias = random.randn() # a random number between -3 and 3, tends to be good for biases

    for i in range(input_layer_size): # for every node in the input layer
      self.input_nodes.append(Node(hidden_layer_size)) # add a node to the list

    for i in range(hidden_layer_size): # for every node in the input layer
      self.hidden_nodes.append(Node(output_layer_size)) # add a node to the list
    
    for i in range(output_layer_size): # for every node in the output layer
      self.output_nodes.append(Node(0)) # add nodes that have no weights coming from them
  
  
  def EmptyNodes(self):

    for node in self.input_nodes:
      node.value = 0
    for node in self.hidden_nodes:
      node.value = 0
    for node in self.output_nodes:
      node.value = 0


  def Predict(self, input_values):

    # console output
    print("A prediction has been made by an AI.")
    
    # empty nodes before making a prediction
    self.EmptyNodes()

    # set the values of the input nodes to be the inputted input values
    for i in range(len(self.input_nodes)):
      self.input_nodes[i].value = input_values[i]
    
    # do feedforward into the hidden layer
    # for every hidden node:
    for current_hidden_node_index in range(len(self.hidden_nodes)):
      # add the bias to the node's value before adding the nodes before it
      self.hidden_nodes[current_hidden_node_index].value += self.hidden_bias
      # for every input node:
      for node in self.input_nodes:
        # for the first hidden node, it uses the first weight, for the second node, uses the second weight etc.
        self.hidden_nodes[current_hidden_node_index].value += node.value * node.weights[current_hidden_node_index]

    # activate
    for node in self.hidden_nodes:
      node.value = round(node.value)

    # do feedforward into the output layer
    # for every output node:
    for current_output_node_index in range(len(self.output_nodes)):
      # add the bias to the node's value before adding the nodes before it
      self.output_nodes[current_output_node_index].value += self.output_bias
      # for every hidden node:
      for node in self.hidden_nodes:
        # for the first output node, it uses the first weight, for the second node, uses the second weight etc.
        self.output_nodes[current_output_node_index].value += node.value * node.weights[current_output_node_index]
    
    # activate
    for node in self.output_nodes:
      node.value = round(node.value)

    # get the output values and return them
    output_values = []
    for node in self.output_nodes:
      output_values.append(node.value)
    return output_values
  

  def Error(self, inputs, target):

    # console output
    print("The error of an AI's answer has been tested.")

    # find how close to the target the network was
    guess = self.Predict(inputs)
    # squared so that negatives go away. it doesnt matter that the number changes
    # because small numbers stay relatively small, and big numbers stay relatively big
    error = 0
    for i in range(len(target)): # target should be the same length as the guess numbers
      error += square(target[i] - guess[i])
    return error
  

  def Display(self, canvas, r):

    # display myself on the tkinter canvas.
    # the width and height of this canvas are hard codes as 800 and 600.
    # the argument r is the radius of the nodes

    # some preemptive text
    canvas.create_text(100, 300, text="Input", font=("Consolas",20), fill="black")
    canvas.create_text(700, 300, text="Output", font=("Consolas",20), fill="black")

    # some variables
    space_between_input_nodes = 600/(len(self.input_nodes)+1)
    space_between_hidden_nodes = 600/(len(self.hidden_nodes)+1)
    space_between_output_nodes = 600/(len(self.output_nodes)+1)

    # show the connections

    # show between input and hidden layers
    for i in range(len(self.input_nodes)):
      input_node_x = 200
      input_node_y = (i+1)*space_between_input_nodes

      for j in range(len(self.hidden_nodes)):
        hidden_node_x = 400
        hidden_node_y = (j+1)*space_between_hidden_nodes
        if self.input_nodes[i].weights[j] < 0:
          colour = "light blue"
        else:
          colour = "orange"
        DrawLine(input_node_x, input_node_y, hidden_node_x, hidden_node_y, round(self.input_nodes[i].weights[j]), colour, canvas)

    # show between hidden and output layers
    for i in range(len(self.hidden_nodes)):
      hidden_node_x = 400
      hidden_node_y = (i+1)*space_between_hidden_nodes

      for j in range(len(self.output_nodes)):
        output_node_x = 600
        output_node_y = (j+1)*space_between_output_nodes
        if self.hidden_nodes[i].weights[j] < 0:
          colour = "light blue"
        else:
          colour = "orange"
        DrawLine(hidden_node_x, hidden_node_y, output_node_x, output_node_y, round(self.hidden_nodes[i].weights[j]), colour, canvas)

    # show the nodes

    # show the input layer
    for i in range(len(self.input_nodes)):
      y = space_between_input_nodes*(i+1)
      canvas.create_oval(200-r, y-r, 200+r, y+r, fill="white")
      text = str(self.input_nodes[i].value)
      canvas.create_text(200, y, text=text, font=("Consolas",12), fill="black")

    # show the hidden layer
    for i in range(len(self.hidden_nodes)):
      y = space_between_hidden_nodes*(i+1)
      canvas.create_oval(400-r, y-r, 400+r, y+r, fill="white")
      text = str(self.hidden_nodes[i].value)
      canvas.create_text(400, y, text=text, font=("Consolas",12), fill="black")

    # show the output layer
    for i in range(len(self.output_nodes)):
      y = space_between_output_nodes*(i+1)
      canvas.create_oval(600-r, y-r, 600+r, y+r, fill="white")
      text = str(self.output_nodes[i].value)
      canvas.create_text(600, y, text=text, font=("Consolas",12), fill="black")