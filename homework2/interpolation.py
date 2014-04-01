import numpy as np
from operator import mul

def createLagrange(x, y):
  def lagrange(z):
    L = range(len(x))
    for i in range(len(x)):
      Li = createLi(x,i)
      L[i] = y[i] * Li(z)
    return sum(L)
  return lagrange

def createLi(xs, i):
  def Li(x):
    prods = [(x-xs[j])/(xs[i]-xs[j]) for j in range(i)] + [(x-xs[j])/(xs[i]-xs[j]) for j in range(i+1, len(xs))]
    return reduce(mul, prods, 1)
  return Li
