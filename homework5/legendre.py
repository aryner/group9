from scipy.integrate import quad
import numpy as np

def generateX(numPoints, start, finish):
  return [((finish-start)/(numPoints-1))*i + start for i in range(numPoints)]

def legendre0(x):
  return 1.

def legendre1(x):
  return x

def legendre2(x):
  return (x**2) - (1./3)

def legendre3(x):
  return x**3 - (3./5)*x

def legendre4(x):
  return x**4 - (6./7)*x**2 + 3./35

def Legendre(k, x):
  if k == 0:
     return legendre0(x)
  elif k == 1:
     return legendre1(x)
  elif k == 2:
     return legendre2(x)
  elif k == 3:
     return legendre3(x)
  elif k == 4:
    return legendre4(x)

def genC(func):
  def square(x):
    return func(x)**2
  return quad(square, -1, 1)

def genAk(k, func):
  def legendre(x):
    return Legendre(k,x)
  def funcLegendre(x):
    return Legendre(k,x) * func(x)
  return (1./genC(legendre)[0]) * quad(funcLegendre, -1, 1)[0]

def genP(k, func):
  def P(x):
    result = 0;
    for i in range(k+1):
      result = result + genAk(k-i,func)*Legendre(k-i,x)
    return result
  return P

