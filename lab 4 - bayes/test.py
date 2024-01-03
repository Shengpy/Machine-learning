import numpy as np
import matplotlib.pyplot as plt
class BayesModel:
  def __init__(self, Hs):
    self.Hs = Hs.copy()
  def update(self, d):
    # update
    s = 0
    for h in self.Hs.keys():
      self.Hs[h] = self.Hs[h] * self.likelihood(h, d)
      s += self.Hs[h]
    # normalize
    for h in self.Hs.keys():
      self.Hs[h] /= s
  def likelihood(self, h, d):
    if h=='covid':
      if d=='+': return 0.98
      if d=='-': return 0.02
    if h=='non-covid':
      if d=='+': return 0.03
      if d=='-': return 0.97
  def plot(self):
    x = list(self.Hs.keys())
    y = list(self.Hs.values())
    plt.bar(x, y)
    plt.ylabel("belief")
    plt.show()
Hs = {'covid': 0.008, 'non-covid': 0.992}
model = BayesModel(Hs)
# model.plot()
model.update('+')
model.plot()
model.update('+')
model.plot()
model.update('+')
model.plot()