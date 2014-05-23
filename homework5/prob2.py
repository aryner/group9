from legendre import *
import numpy as np
import matplotlib.pyplot as plt

x = [0.01,0.9998,2.1203,3.0023,3.9892,5.0017]
y = [0.9631,0.5221,0.233,0.1248,0.0107,0.0065]

def func(a,b,x):
  return b*np.e**(a*x)

def normal1(x, y, a, b):
  return (y-b*np.e**(a*x))*x*np.e**(a*x)

def normal2(x, y, a, b):
  return y-b*np.e**(a*x)

def f1a(x,y,a,b):
  return x**2*np.e**(a*x)*(y-2*b*np.e**(a*x))

def f1b(x,y,a,b):
  return x*np.e**(2*a*x)

def f2a(x,y,a,b):
  return -b*x*np.e**(a*x)

def f2b(x,y,a,b):
  return -np.e**(a*x)

def inverseJacobi(a,b):
  topLeft = sum([f1a(x[i],y[i],a,b) for i in range(len(x))])
  topRight = sum([f1b(x[i],y[i],a,b) for i in range(len(x))])
  botLeft = sum([f2a(x[i],y[i],a,b) for i in range(len(x))])
  botRight = sum([f2b(x[i],y[i],a,b) for i in range(len(x))])

  j = np.matrix([[topLeft,topRight],[botLeft,botRight]])

  return j.I

def tolerance(g1,g2):
  top = np.maximum(abs(g2[0]-g1[0]),abs(g2[1]-g1[1]))
  bot = np.maximum(abs(g2[0]), abs(g2[1]))
  return top/bot

guess = [-1.,1.]

while(1 == 1):
  J = inverseJacobi(guess[0],guess[1])
  f1 = sum([normal1(x[i],y[i],guess[0],guess[1]) for i in range(len(x))])
  f2 = sum([normal2(x[i],y[i],guess[0],guess[1]) for i in range(len(x))])
  deltaX = -J*np.matrix([[f1],[f2]])
  oldGuess = guess
  deltaX = deltaX.A1
  guess = [guess[0]+deltaX[0], guess[1]+deltaX[1]]

  if(tolerance(oldGuess,guess) < .00001):
    break

x1 = generateX(100, -0.1, 5.1)
y1 = [func(guess[0],guess[1],x1[i]) for i in range(len(x1))]


plt.figure(1)
plt.plot(x,y)
plt.plot(x1,y1)
plt.show()

'''
mat = np.matrix([[1,2],[3,4]])
print mat
mat2 = mat.I
print mat2
'''

'''
p = np.polynomial.polynomial.polyval(2,[1,2,3,])
print p
'''


