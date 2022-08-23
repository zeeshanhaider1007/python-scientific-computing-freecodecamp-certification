import copy
import random
# Consider using the modules imported above.

import random
from collections import Counter

class Hat:
  def __init__(self,**kwargs):
    self.contents = []
    for key,value in kwargs.items():
      self.contents.extend([key]*value)
  def draw(self, n):
    array = range(len(self.contents))
    if n >= len(self.contents):
      return self.contents.copy()
    else:
      drawn = []
      numbers = random.sample(array,n)
      for i in numbers:
        drawn.append(self.contents[i])
        self.contents[i] = -1
      while -1 in self.contents:
        self.contents.remove(-1)
      return drawn
      
def experiment(hat, expected_balls,
              num_balls_drawn,
              num_experiments):

  N = num_experiments
  M = 0
  for i in range(N):
    drawn = copy.deepcopy(hat).draw(num_balls_drawn)
    drawn = Counter(drawn)
    if all(item[0] in drawn and drawn[item[0]]>=item[1]  for item in expected_balls.items()):
      M+=1

  return M/N
    