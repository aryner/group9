from legendre import *
import numpy as np
import matplotlib.pyplot as plt

def f(x):
  if x <= -0.5:
    return 0.
  elif x < 0.5:
    return 1.
  else:
    return 0.

def ex(x):
  return np.e**x

P = genP(4, ex)
print P(0.5)
print ex(0.5)

x = generateX(400,  -1., 1.)
y = [f(i) for i in x]

#plt.figure(1)
#plt.plot(x, y)
#plt.show()
