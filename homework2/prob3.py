from interpolation import *
import numpy as np
import matplotlib.pyplot as plt

x = [0.,1./6,1./3,1./2,7./12,2./3,3./4,5./6,11./12,1.]
x1 = np.arange(0.,1.,0.001)
x2 = np.arange(0.,1.,0.01)

def f(x):
  return 1.6*np.e**(-2*x)*np.sin(3*np.pi*x)

def df(x):
  return np.e**(-2*x)*(15.0796*np.cos(3*np.pi*x)-3.2*np.sin(3*np.pi*x))

y = [f(i) for i in x]
y1 = [f(i) for i in x2]
y2 = [df(i) for i in x1]

lagrange = createLagrange(x,y)
y3 = [lagrange(i) for i in x2]
hermiteCoefficients(x,[f(i) for i in x], [df(i) for i in x])

#plt.plot(x2, y1, 'g')
#plt.plot(x, y, 'ro')
#plt.plot(x2, y3, 'b')
#plt.show()
