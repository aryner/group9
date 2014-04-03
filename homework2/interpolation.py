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

def hermiteCoefficients(x, fx, dfx):
  z = range(len(x)*2)
  Q = range(len(z))

  for i in range(len(z)):
    Q[i] = range(len(z))

  for i in range(len(x)):
    z[i*2] = x[i]
    z[i*2+1] = x[i]
    Q[i*2][0] = fx[i]
    Q[i*2+1][0] = fx[i]
    Q[i*2+1][1] = dfx[i]

  for i in range(1,len(x)):
    Q[2*i][1] = (Q[2*i][0] - Q[2*i-1][0]) / (z[2*i] - z[2*i-1])

  for i in range(2, len(z)):
    for j in range(2, i+1):
      Q[i][j] = (Q[i][j-1] - Q[i-1][j-1]) / (z[i] - z[i-j])

  return [Q[i][i] for i in range(len(z))]

def completeHermite(Q,xs):
  def func(x):
    H = range(len(Q))
    H[0] = Q[0]
    factors = range(len(xs))

    for i in range(len(xs)):
      factors[i] = (x - xs[i])
 
    for i in range(1,len(Q)):
      H[i] = Q[i]
      for j in range(i):
        H[i] = H[i] * factors[j/2]
    return sum(H)
  return func
