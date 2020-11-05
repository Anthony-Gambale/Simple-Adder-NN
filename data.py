
from random import randint

exam = []
exam_length = 200
for i in range(exam_length):
  a = randint(-10, 10)
  b = randint(-10, 10)
  exam.append([a, b, a+b])

def Fitness(network):

  # console output
  print("The fitness of an AI has been tested.")

  total_error = 0

  for question in exam:
    total_error += network.Error([question[0], question[1]], [question[2]])
  
  if total_error == 0:
    return 99999999
  else:
    return 1/total_error
