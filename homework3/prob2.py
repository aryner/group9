from numericalIntegrals import *
import numpy as np
import matplotlib.pyplot as plt

def sinPi(x):
  return np.sin(np.pi*x)

def eToSomeCrap(x):
  return np.e**((-(x)**2)/2)

def sinC(x):
  if x == 0:
    return 1
  else:
    return (np.sin(2*np.pi*x))/(2*np.pi*x)

numPoints = 5050000
x = generateX(numPoints, 0, 0.5)
y = [sinPi(x[i]) for i in range(0,numPoints)]

one = 1/np.pi
print 1/np.pi - trapezoidal(x,y)
print 1/np.pi - romberg(0, 0.5, 1675000, sinPi)
print 1/np.pi - gaussQuadrature(0, 0.5, sinPi, 4)
print ""
plt.figure(1)
plt.title('a')
xp1 = generateX(100,0,0.5)
yp1 = [sinPi(xp1[i]) for i in range(0,100)]
plt.plot(xp1,yp1,'b')

numPoints2 = 1500000
x2 = generateX(numPoints2, 1.,2.)
y2 = [eToSomeCrap(x2[i]) for i in range(0, numPoints2)]

two = 0.3406636214304
print two - trapezoidal(x2,y2)
print two - romberg(1.,2., 500000, eToSomeCrap)
print two - gaussQuadrature(1.,2.,eToSomeCrap, 4)
print ""
plt.figure(2)
plt.title('b')
xp2 = generateX(100,1.,2.)
yp2 = [eToSomeCrap(xp2[i]) for i in range(0,100)]
plt.plot(xp2,yp2,'b')

numPoints3 = 7000
x3 = generateX(numPoints3, -1.,1.)
y3 = [sinC(x3[i]) for i in range(0, numPoints3)]

three = 0.45141166679014
print three - trapezoidal(x3,y3)
print three - romberg(-1.,1., 310, sinC)
print three - gaussQuadrature(-1.,1., sinC, 9)
plt.figure(3)
plt.title('c')
xp3 = generateX(100,-1.,1.)
yp3 = [eToSomeCrap(xp3[i]) for i in range(0,100)]
plt.plot(xp3,yp3,'b')
plt.show()

