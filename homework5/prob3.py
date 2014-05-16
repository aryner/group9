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

P0 = genP(0, f)
P1 = genP(1, f)
P2 = genP(2, f)
P3 = genP(3, f)
P4 = genP(4, f)
P1(1)

x1 = generateX(400,  -1., 1.)
x2 = generateX(600, -1.25, 1.25)
y = [f(i) for i in x1]
y0 = [P0(i) for i in x2]
y1 = [P1(i) for i in x2]
y2 = [P2(i) for i in x2]
y3 = [P3(i) for i in x2]
y4 = [P4(i) for i in x2]

plt.figure(1)
plt.plot(x1, y)
plt.plot(x2, y0)
plt.plot(x2, y1)
plt.plot(x2, y2)
plt.plot(x2, y3)
plt.plot(x2, y4)
plt.show()
