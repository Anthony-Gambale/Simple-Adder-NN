
# imports
import network as nt
import world as w
from data import data

# varaibles
populationSize = 10000
matingPoolSize = 30

# inits
earth = w.World(populationSize)

# learning loop
while True:
   earth.SortPopulation() # sort the population
   print('The current best thinks that 3 + 4 = ' + str(earth.population[0].Guess([3, 4]))) # make a guess on data you have not been tested on
   earth.Repopulate(matingPoolSize, populationSize) # make a new population