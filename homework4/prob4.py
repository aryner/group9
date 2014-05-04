from newton import *
import numpy as np
import matplotlib.pyplot as plt

eqn1 = [[[3,2]],[[-1,2]]]
eqn2 = [[[-1,2]],[['3x',2],[-1,0]]]

def one(x):
  return (3.*x**2.)**(1./2)
def dOne(x):
  return ((3.**(1./2))*x)/((x**2.)**(1./2))
def two(x):
  return ((1.+x**2.)/(3.*x))**(1./2)
def dTwo(x):
  return -(x**2.+1.)/(2.+(3.**(1./2))*(((1./x)-x)**(1./2))*x**2.)

def oneMtwo(x):
  return one(x) - two(x)
def dOneMdTwo(x):
  return dOne(x) - dTwo(x)

print '***Solving using the two dimensional version of Newtons method***'
print '\t\tOur equations are:'
print2d(eqn1)
print ' = 0'
print2d(eqn2)
print ' = 0'
print
print 'The first iteration of Newtons methdo using a guess of [1,1] gives us:'
X1 = newton2d(eqn1,eqn2, [1,1])
print X1
print
print 'using the infinity norm our error is:'
print infinTol([1,1],X1)
print '...'
print 'Iteration 2:'
X2 = newton2d(eqn1,eqn2, X1)
print X2
print 'Error: ', infinTol(X1,X2)
print '...'
print 'Iteration 3:'
X3 = newton2d(eqn1,eqn2, X2)
print X3
print 'Error: ', infinTol(X2,X3)
print '...'
print 'Iteration 4:'
X4 = newton2d(eqn1,eqn2, X3)
print X4
print 'Error: ', infinTol(X3,X4)
print '...'
print 'Iteration 5:'
X5 = newton2d(eqn1,eqn2, X4)
print X5
print 'Error: ', infinTol(X4,X5)
print '...'
print 'Iteration 6:'
X6 = newton2d(eqn1,eqn2, X5)
print X6
print 'Error: ', infinTol(X5,X6)
print '...'
print 'Iteration 7:'
X7 = newton2d(eqn1,eqn2, X6)
print X7
print 'Error: ', infinTol(X6,X7)
print '...'
print 'Iteration 8:'
X8 = newton2d(eqn1,eqn2, X7)
print X8
print 'Error: ', infinTol(X7,X8)
print '...'
print 'Iteration 9:'
X9 = newton2d(eqn1,eqn2, X8)
print X9
print 'Error: ', infinTol(X8,X9)
print
print '***Solving by using the one dimensional method***'
y = oneMtwo(1)
print 'For this case f(x) is first equation minus the second equation'
print 'for the first iterations we will guess the x value is 1, which makes the f(1)= ', y
x1 = newton(oneMtwo,dOneMdTwo,1)
print 'which gives us the x1: ', x1
print
print 'using the infinity norm our error is:'
print singleTol(1,x1)
print '...'
print 'Iteration 2:'
print 'f(x1) = ', oneMtwo(x1)
x2 = newton(oneMtwo,dOneMdTwo,x1)
print 'x2 = ', x2
print 'Error: ', singleTol(x1,x2)
print '...'
print 'Iteration 3:'
print 'f(x2) = ', oneMtwo(x2)
x3 = newton(oneMtwo,dOneMdTwo,x2)
print 'x3 = ', x3
print 'Error: ', singleTol(x2,x1)
print '...'
print 'Iteration 4:'
print 'f(x3) = ', oneMtwo(x3)
x4 = newton(oneMtwo,dOneMdTwo,x3)
print 'x4 = ', x4
print 'Error: ', singleTol(x4,x3)
print '...'
print 'Iteration 5:'
print 'f(x4) = ', oneMtwo(x4)
x5 = newton(oneMtwo,dOneMdTwo,x4)
print 'x5 = ', x5
print 'Error: ', singleTol(x5,x4)
print '...'
print 'Iteration 6:'
print 'f(x5) = ', oneMtwo(x5)
x6 = newton(oneMtwo,dOneMdTwo,x5)
print 'x6 = ', x6
print 'Error: ', singleTol(x6,x5)
print '...'
print 'Iteration 7:'
print 'f(x6) = ', oneMtwo(x6)
x7 = newton(oneMtwo,dOneMdTwo,x6)
print 'x7 = ', x7
print 'Error: ', singleTol(x7,x6)
print '...'
print 'Iteration 8:'
print 'f(x7) = ', oneMtwo(x7)
x8 = newton(oneMtwo,dOneMdTwo,x7)
print 'x8 = ', x8
print 'Error: ', singleTol(x8,x7)
print '...'
print 'Iteration 9:'
print 'f(x8) = ', oneMtwo(x8)
x9 = newton(oneMtwo,dOneMdTwo,x8)
print 'x9 = ', x9
print 'Error: ', singleTol(x9,x8)

x = generateX(100,0.1,.8)
y1 = [one(x[i]) for i in range(len(x))]
y2 = [two(x[i]) for i in range(len(x))]
y3 = [oneMtwo(x[i]) for i in range(len(x))]

plt.figure(1)
plt.title('eqn1-eqn2 and the single dimension approximation')
plt.plot([x9,x9], [-.25,.25])
plt.plot(x,[0 for i in range(len(x))])
plt.plot(x,y3)

plt.figure(2)
plt.title('eqn1 and eqn2 with the two dimensional approximation')
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot([X9[0],X9[0]] , [.8,1])
plt.plot([X9[0]-.05,X9[0]+.05], [X9[1],X9[1]] )
plt.show()

