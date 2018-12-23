
'''imports'''
import numpy as np

'''network class'''
class Network:

   # constructor
   def __init__(self):
      self.w1 = np.random.randn()
      self.w2 = np.random.randn()
      self.w3 = np.random.randn()
      self.w4 = np.random.randn()
      self.w5 = np.random.randn()
      self.w6 = np.random.randn()
      self.b1 = np.random.randn()
      self.b2 = np.random.randn()

   # guess function
   def Guess(self, point):
      hidden0 = point[0] * self.w1 + point[1] * self.w2 + self.b1
      hidden1 = point[0] * self.w3 + point[1] * self.w4 + self.b1
      prediction = hidden0 * self.w5 + hidden1 * self.w6 + self.b2
      return prediction
   
   # cost function
   def Cost(self, point):
      prediction = self.Guess(point)
      target = point[2]
      return np.square(target - prediction)