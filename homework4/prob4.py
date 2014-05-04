from newton import *
import numpy as np
import matplotlib.pyplot as plt

eqn1 = [[[3,2]],[[-1,2]]]
eqn2 = [[[-1,2]],[['3x',2],[-1,0]]]

print '***Solving using the two dimensional version of Newtons method***'
print '\t\tOur equations are:'
print2d(eqn1)
print ' = 0'
print2d(eqn2)
print ' = 0'
print
print 'The first iteration of Newtons methdo using a guess of [1,1] gives us:'
x1 = newton2d(eqn1,eqn2, [1,1])
print x1
print
print 'using the infinity norm our error is:'
print infinTol([1,1],x1)
print '...'
print 'Iteration 2:'
x2 = newton2d(eqn1,eqn2, x1)
print x2
print 'Error: ', infinTol(x1,x2)
print '...'
print 'Iteration 3:'
x3 = newton2d(eqn1,eqn2, x2)
print x3
print 'Error: ', infinTol(x2,x3)
print '...'
print 'Iteration 4:'
x4 = newton2d(eqn1,eqn2, x3)
print x4
print 'Error: ', infinTol(x3,x4)
print '...'
print 'Iteration 5:'
x5 = newton2d(eqn1,eqn2, x4)
print x5
print 'Error: ', infinTol(x4,x5)
print
print '***Solving by using the one dimensional method***'
