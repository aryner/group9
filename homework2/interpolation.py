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

def hermite(x, fx, dfx):
  Q = hermiteCoefficients(x, fx, dfx)
  return completeHermite(Q, x)

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

def cubicSpline(xs, fx):
  a,b,c,d = cubicSplineUnknowns(xs, fx)
  def func(x):
    if x > xs[len(xs)-1]:
      return a[len(xs)-2] + b[len(xs)-2]*(x-xs[len(xs)-2]) + c[len(xs)-2]*(x-xs[len(xs)-2])**2 + d[len(xs)-2]*(x-xs[len(xs)-2])**3

    for i in range(len(a)-1):
      if x < xs[i+1]:
        return a[i] + b[i]*(x-xs[i]) + c[i]*(x-xs[i])**2 + d[i]*(x-xs[i])**3
  return func

def cubicSplineUnknowns(x, fx):
  a = fx

  h = range(len(x)-1)
  for i in range(len(x)-1):
    h[i] = x[i+1] - x[i]

  alpha = range(len(x)-1)
  for i in range(1, len(x)-1):
    alpha[i] = (3/h[i])*(a[i+1]-a[i]) - (3/h[i-1])*(a[i]-a[i-1])

  l = range(len(x))
  u = range(len(x)-1)
  z = range(len(x))
  for i in range(1, len(x)-1):
    l[i] = 2*(x[i+1] - x[i-1]) - h[i-1] * u[i-1]
    u[i] = h[i] / l[i]
    z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]

  l[len(x)-1] = 1
  z[len(x)-1] = 0

  b = range(len(x)-1)
  c = range(len(x))
  d = range(len(x)-1)
  c[len(c)-1] = 0
  L = range(len(x)-1)
  for i in L[::-1]:
    c[i] = z[i] - u[i] * c[i+1]
    b[i] = (a[i+1] - a[i]) / h[i] - h[i]*(c[i+1] + 2*c[i])/3
    d[i] = (c[i+1] - c[i]) / (3*h[i])

  return a[:len(x)-1], b, c[:len(x)-1], d

def linearSpline(xs, fx):
  def func(x):
    yPsi = range(len(fx))
    for i in range(len(fx)):
      yPsi[i] = fx[i] * psi(x, xs, i)
    return sum(yPsi)
  return func

def psi(x, xs, i):
  if i == 0:
    return theta1((x-xs[0])/(xs[1]-xs[0]))
  if i == len(xs)-1:
    return theta2((x-xs[len(xs)-1])/(xs[len(xs)-1]-xs[len(xs)-2]))
  return theta2((x-xs[i-1])/(xs[i]-xs[i-1])) + theta1((x-xs[i])/(xs[i+1]-xs[i]))

def theta1(x):
  if x >= 0  and x < 1:
    return 1-x
  return 0

def theta2(x):
  if x >= 0  and x < 1:
    return x
  return 0

