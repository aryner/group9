from interpolation import *
import numpy as np
import matplotlib.pyplot as plt

lineX1 = np.arange(-0.025,1.085,0.001)
lineX2 = np.arange(-0.11,1.15,0.001)
lineY1 = [0 for i in lineX1]
lineY2 = [0 for i in lineX2]

x = [0.,1./6,1./3,1./2,7./12,2./3,3./4,5./6,11./12,1.]
x1 = np.arange(-0.025,1.085,0.001)
x2 = np.arange(-0.11,1.15,0.001)

def f(x):
  return 1.6*np.e**(-2*x)*np.sin(3*np.pi*x)
def df(x):
  return np.e**(-2*x)*(15.0796*np.cos(3*np.pi*x)-3.2*np.sin(3*np.pi*x))

y = [f(i) for i in x]
y1 = [f(i) for i in x1]
y2 = [f(i) for i in x2]
dy = [df(i) for i in x]

lagrange = createLagrange(x,y)
Ly = [lagrange(i) for i in x2]
diff = differenceFunction(lagrange, f)
LyDiff = [diff(i) for i in x2]

hermiteF = hermite(x, y, dy)
Hy = [hermiteF(i) for i in x1]
diff = differenceFunction(hermiteF, f)
Hdiff = [diff(i) for i in x1]

cubicSplineF = cubicSpline(x, y)
cSy = [cubicSplineF(i) for i in x2]
diff = differenceFunction(cubicSplineF, f)
cubicDiff = [diff(i) for i in x2]

linearSplineF = linearSpline(x,y)
lSy = [linearSplineF(i) for i in x2]
diff = differenceFunction(linearSplineF, f)
linearDiff = [diff(i) for i in x2]


plt.figure(1)
plt.subplot(211)
plt.title('Linear Spline vs. f(x)')
plt.plot(x2,y2,'b')
plt.plot(x2, lSy, 'g')
plt.subplot(212)
plt.title('Diffrence function')
plt.plot(x2, linearDiff, 'g')
plt.plot(lineX2, lineY2, 'b')

plt.figure(2)
plt.subplot(221)
plt.title('Lagrange vs f(x)')
plt.plot(x2,Ly,'b')
plt.plot(x2,y2,'g')
plt.subplot(223)
plt.title('Left Quarter diffrenence')
plt.plot(x2[(len(lineX2)/20)*2:(len(lineX2)/4)],LyDiff[(len(lineX2)/20)*2:(len(lineX2)/4)], 'g')
plt.plot(lineX2[(len(lineX2)/20)*2:(len(lineX2)/4)],lineY2[(len(lineX2)/20)*2:(len(lineX2)/4)], 'b')
plt.subplot(224)
plt.title('Right Quarter difference')
plt.plot(x2[3*(len(lineX2)/4):len(lineX2) - (len(lineX2)/20)*2],LyDiff[3*(len(lineX2)/4):len(lineX2) - (len(lineX2)/20)*2], 'g')
plt.plot(lineX2[3*(len(lineX2)/4):len(lineX2) - (len(lineX2)/20)*2],lineY2[3*(len(lineX2)/4):len(lineX2) - (len(lineX2)/20)*2], 'b')
plt.subplot(222)
plt.title('Middle half difference')
plt.plot(x2[len(lineX2)/4:3*(len(lineX2)/4)],LyDiff[(len(lineX2)/4):3*(len(lineX2)/4)], 'g')
plt.plot(lineX2[len(lineX2)/4:3*(len(lineX2)/4)],lineY2[(len(lineX2)/4):3*(len(lineX2)/4)], 'b')

plt.figure(3)
plt.subplot(221)
plt.title('Hermite vs f(x)')
plt.plot(x1,Hy,'b')
plt.plot(x1,y1,'g')
plt.subplot(223)
plt.title('Left Quarter diffrenence')
plt.plot(x2[(len(lineX1)/20)*2:(len(lineX1)/4)],Hdiff[(len(lineX1)/20)*2:(len(lineX1)/4)], 'g')
plt.plot(lineX1[(len(lineX1)/20)*2:(len(lineX1)/4)],lineY1[(len(lineX1)/20)*2:(len(lineX1)/4)], 'b')
plt.subplot(224)
plt.title('Right Quarter difference')
plt.plot(x1[3*(len(lineX1)/4):len(lineX1) - (len(lineX1)/20)*2],Hdiff[3*(len(lineX1)/4):len(lineX1) - (len(lineX1)/20)*2], 'g')
plt.plot(lineX1[3*(len(lineX1)/4):len(lineX1) - (len(lineX1)/20)*2],lineY1[3*(len(lineX1)/4):len(lineX1) - (len(lineX1)/20)*2], 'b')
plt.subplot(222)
plt.title('Middle half difference')
plt.plot(x1[len(lineX1)/4:3*(len(lineX1)/4)],Hdiff[(len(lineX1)/4):3*(len(lineX1)/4)], 'g')
plt.plot(lineX1[len(lineX1)/4:3*(len(lineX1)/4)],lineY1[(len(lineX1)/4):3*(len(lineX1)/4)], 'b')

plt.figure(4)
plt.subplot(221)
plt.title('Cubic Spline vs f(x)')
plt.plot(x2,Ly,'b')
plt.plot(x2,y2,'g')
plt.subplot(223)
plt.title('Left Quarter diffrenence')
plt.plot(x2[(len(lineX2)/20)*2:(len(lineX2)/4)],cubicDiff[(len(lineX2)/20)*2:(len(lineX2)/4)], 'g')
plt.plot(lineX2[(len(lineX2)/20)*2:(len(lineX2)/4)],lineY2[(len(lineX2)/20)*2:(len(lineX2)/4)], 'b')
plt.subplot(224)
plt.title('Right Quarter difference')
plt.plot(x2[3*(len(lineX2)/4):len(lineX2) - (len(lineX2)/20)*2],cubicDiff[3*(len(lineX2)/4):len(lineX2) - (len(lineX2)/20)*2], 'g')
plt.plot(lineX2[3*(len(lineX2)/4):len(lineX2) - (len(lineX2)/20)*2],lineY2[3*(len(lineX2)/4):len(lineX2) - (len(lineX2)/20)*2], 'b')
plt.subplot(222)
plt.title('Middle half difference')
plt.plot(x2[len(lineX2)/4:3*(len(lineX2)/4)],cubicDiff[(len(lineX2)/4):3*(len(lineX2)/4)], 'g')
plt.plot(lineX2[len(lineX2)/4:3*(len(lineX2)/4)],lineY2[(len(lineX2)/4):3*(len(lineX2)/4)], 'b')

plt.show()
