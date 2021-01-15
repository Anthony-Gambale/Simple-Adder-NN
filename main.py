'''
Adder Neural Network by Anthony Gambale January 2019

Two tabs. One for buttons and sliders for editing the NN, one for
displaying the visualised network.
'''

'''
IMPORTS
'''
from tkinter import *
from tkinter import ttk
from network import *
from random import randint
from data import Fitness

'''
SETUP
window and tab setup
'''
window = Tk()
window.geometry("800x640")
window.title("Visual Neural Network VERSION 1.0")
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Neural Network')
tab_control.add(tab2, text='Dashboard')
canvas = Canvas(tab1, width=800, height=640)
canvas.pack()
mainNetwork = Network(2, 1, 1)

'''
TEST FUNCTION
The function for the button.
'''
def Test(network):
  a = randint(-10, 10)
  b = randint(-10, 10)
  network.Predict([a, b])
  canvas.delete("all")
  network.Display(canvas, 15)

'''
RESET FUNCTION
The function for the button.
'''
def Reset():
  h = slider.get()
  global mainNetwork
  mainNetwork = Network(2, h, 1)

  canvas.delete("all")
  mainNetwork.Display(canvas, 15)


'''
TRAIN FUNCTION
The function for the button.
'''
def Train():

  global mainNetwork
  current_best = Fitness(mainNetwork)

  newNetwork = Network(2, len(mainNetwork.hidden_nodes), 1)

  while Fitness(newNetwork) < current_best:
    newNetwork = Network(2, len(mainNetwork.hidden_nodes), 1)

  mainNetwork = newNetwork
  canvas.delete("all")
  mainNetwork.Display(canvas, 15)

'''
CONTENTS
contents of the dashboard tab
'''
sliderText = Label(tab2, text= 'Number of Nodes in middle layer (you must reset to take effect)')
sliderText.grid(column=0, row=3)
slider = Scale(tab2, from_=1, to=17, orient=HORIZONTAL)
slider.grid(column=1, row=3)

resetText = Label(tab2, text= 'Reset the network to a randomly generated one:')
resetText.grid(column=0, row=4)
resetButton = Button(tab2, text='Reset', command=Reset)
resetButton.grid(column=1, row=4)

trainText = Label(tab2, text= 'Randomly generate networks until a better one is found:')
trainText.grid(column=0, row=5)
trainButton = Button(tab2, text='Train', command=Train)
trainButton.grid(column=1, row=5)

testText = Label(tab2, text= 'Guess the sum of 2 random numbers:')
testText.grid(column=0, row=6)
testButton = Button(tab2, text='Guess', command= lambda: Test(mainNetwork))
testButton.grid(column=1, row=6)

Explanation1 = Label(tab2, text='Orange lines have positive weights, blue have negative.')
Explanation1.grid(column=0, row=0)

Explanation2 = Label(tab2, text='Thick lines have larger weights, thin lines have smaller weights.')
Explanation2.grid(column=0, row=1)

Explanation3 = Label(tab2, text='If a line is not drawn, the weight is between -0.5 and 0.5')
Explanation3.grid(column=0, row=2)

'''
DRAW
the draw step
'''
mainNetwork.Display(canvas, 15)

'''
MAIN LOOP
main loop of the window
'''
tab_control.pack(expand=1, fill='both')
window.mainloop()
