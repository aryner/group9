import numpy as np

def gaussPoints(n):
  if n == 2:
    return [0.57735029692, -0.5773502692]
  elif n == 3:
    return [0.7745966692, 0, -0.7745966692]
  elif n == 4:
    return [0.8611363116, 0.3399810436, -0.3399810436, -0.8611363116]
  else:
    return [0.9061798459, 0.5384693101, 0, -0.5384693101, -0.9061798459]

def gaussWeights(n):
  if n == 2:
    return [1,1]
  elif n == 3:
    return [0.5555555556, 0.8888888889, 0.5555555556]
  elif n == 4:
    return [0.3478548451, 0.6521451549, 0.6521451549, 0.3478548451]
  else:
    return [0.2369268850, 0.4786286705, 0.5688888889, 0.4786286705, 0.2369268850]

def generateX(numPoints, start, finish):
  return [((finish-start)/(numPoints-1))*i+start for i in range(numPoints)]

def trapezoidal(x, y):
  return ((x[1]-x[0])/2)*(y[0] + 2 * np.sum([y[i] for i in range(1,len(y)-2)]) + y[len(y)-1])

def romberg(start, end, firstNumPoints, func):
  x1 = generateX(firstNumPoints, start, end)
  y1 = [func(x1[i]) for i in range(0,firstNumPoints)]
  x2 = generateX(firstNumPoints*2, start,end)
  y2 = [func(x2[i]) for i in range(0,firstNumPoints*2)]

  trap1 = trapezoidal(x1,y1)
  trap2 = trapezoidal(x2,y2)

  return trap2 + (trap2-trap1) / 3

def gaussQuadrature(a, b, func, numPoints):
  def t(x):
    return 0.5*((b-a)*x+a+b)
  scale = (b-a)/2

  x = gaussPoints(numPoints)
  w = gaussWeights(numPoints)

  terms = [func(t(x[i]))*w[i]*scale for i in range(len(x))]
  return sum(terms)
