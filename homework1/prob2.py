from gauss import *

matrix = [
          [10.,10.,10.,1e17,1e17],
          [1.,1e-3,1e-3,1e-3,1.],
          [1.,1.,1e-3,1e-3,2.],
          [1.,1.,1.,1e-3,3.]
          ]

matrix1 = [
          [10,10,10,1e17],
          [1,1e-3,1e-3,1e-3],
          [1,1,1e-3,1e-3],
          [1,1,1,1e-3]
          ]

print '***The matrix in question:***'
show(matrix)
a = rowReduce(matrix)
a = backSub(a)
print '\na) using basic Gaussian elemination we get:'
show(a)

b = rowReducePartialPivots(matrix)
b = backSub(b)
print '\nb) using Gaussian elemination with partial pivoting we get:'
show(b)

c = scaledPartialRowReduce(matrix)
c = backSub(c)
print '\nc) using Gaussian elimination with partially scaled pivoting we get:' 
show(c)
"""
print '\nExamining why we get the wrong answer with part a, '
print 'lets look at the reduced matrix using naive elemination'

d = rowReduce(matrix)
backSubTrace(d)
"""

