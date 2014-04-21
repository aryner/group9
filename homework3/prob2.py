from numericalIntegrals import *
import numpy as np
import matplotlib.pyplot as plt

def sinPi(x):
  return np.sin(np.pi*x)

def eToSomeCrap(x):
  return e**(((-x)**2)/2)

def sinC(x):
  if x == 0:
    return 1
  else:
    return (np.sin(2*np.pi*x))/(2*np.pi*x)

numPoints = 10
x = generateX(numPoints, 0, 0.5)
y = [sinPi(x[i]) for i in range(0,numPoints)]

print trapezoidal(x,y)
print romberg(0, 0.5, 5, sinPi)
print gaussQuadrature(0, 0.5, sinPi, 2)

