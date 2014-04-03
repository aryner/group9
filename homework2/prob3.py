from interpolation import *
import numpy as np
import matplotlib.pyplot as plt

x = [0.,1./6,1./3,1./2,7./12,2./3,3./4,5./6,11./12,1.]
x1 = np.arange(-0.025,1.085,0.001)
x2 = np.arange(-0.11,1.15,0.001)

def f(x):
  return 1.6*np.e**(-2*x)*np.sin(3*np.pi*x)

def df(x):
  return np.e**(-2*x)*(15.0796*np.cos(3*np.pi*x)-3.2*np.sin(3*np.pi*x))

y = [f(i) for i in x]
y1 = [f(i) for i in x2]
y2 = [df(i) for i in x]

lagrange = createLagrange(x,y)
y3 = [lagrange(i) for i in x2]

hermite = hermite(x, y, y2)
y4 = [hermite(i) for i in x1]

cubicSpline = cubicSpline(x, y)
y5 = [cubicSpline(i) for i in x2]

linearSpline = linearSpline(x,y)
y6 = [linearSpline(i) for i in x2]

plt.plot(x2, y1, 'g')
plt.plot(x, y, 'ro')
plt.plot(x2, y6, 'b')
plt.plot(x1, y4, 'y')
plt.show()
