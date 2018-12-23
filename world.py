'''

This python file handles a world filled with neural networks and their evolution.

This file has 3 purposes:
1. Generate a population of neural networks with random weights and biases
2. Calculate how fit each neural network is (by adding up the cost of all of their predictions over all the data)
3. Repopulate with a new population of neural networks whose weights and biases are taken from the fittest of the
previous generation.

'''

import network as nt
from random import randint
from data import data

class World:

   # constructor
   def __init__(self, n):

      # variables
      self.population = []
      self.matingPool = []
      # fill population
      for i in range(n):
         self.population.append(nt.Network())
   
   # find the fitness of a single network
   def Fitness(self, network):
      # calculate the total error
      totalError = 0
      for point in data:
         totalError += network.Cost(point)
      # the smaller the error, the better
      # the bigger the fitness, the better
      # by doing 1/error, it means that if your error is smaller, your fitness is bigger
      return 1/totalError
   
   # sort the population into fitness order using an insertion sort algorithm
   def SortPopulation(self):
      for i in range(1, len(self.population)):
         for j in range(i-1, 0, -1):
            if self.Fitness(self.population[j]) > self.Fitness(self.population[j-1]):
               self.population[j], self.population[j-1] = self.population[j-1], self.population[j]
            
   # make a new population based on an inputted number of parents
   def Repopulate(self, p, n):
      # empty and fill the mating pool
      self.matingPool = []
      for i in range(p):
         self.matingPool.append(self.population[i])
      # empty and fill the population
      self.population = []
      for i in range(n):
         child = nt.Network()
         child.w1 = self.matingPool[randint(0, p-1)].w1
         child.w2 = self.matingPool[randint(0, p-1)].w2
         child.w3 = self.matingPool[randint(0, p-1)].w3
         child.w4 = self.matingPool[randint(0, p-1)].w4
         child.w5 = self.matingPool[randint(0, p-1)].w5
         child.w6 = self.matingPool[randint(0, p-1)].w6
         child.b1 = self.matingPool[randint(0, p-1)].b1
         child.b2 = self.matingPool[randint(0, p-1)].b2
         self.population.append(child)