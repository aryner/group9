from gauss import *

matrix = [
          [10.,10.,10.,1e17,1e17],
          [1.,1e-3,1e-3,1e-3,1.],
          [1.,1.,1e-3,1e-3,2.],
          [1.,1.,1.,1e-3,3.]
          ]

print '***The matrix in question:***'
show(matrix)
a = rowReduce(matrix)
A = a
a = backSub(a)
print '\na) using basic Gaussian elemination we get:'
show(a)

b = rowReducePartialPivots(matrix)
b = backSub(b)
print '\nb) using Gaussian elemination with partial pivoting we get:'
show(b)

c = scaledPartialRowReduce(matrix)
C = c
c = backSub(c)
print '\nc) using Gaussian elimination with partially scaled pivoting we get:' 
show(c)

print '\nwe get the same answer in part a and be because zeroing out'
print 'the first column below position 1,1 completely row reduces '
print 'the matrix so it makes no diffrence if we use partial pivots'
print '\nKnowing this the resdual error vector for both a and b is:'
show(resErrorVector(matrix,b))
print '\nand the residual error vector for part c is:'
show(resErrorVector(matrix,c))

print '\nSo using partially scaled pivoting we get very close to the answer, '
print 'but with basic Gaussian elimination we do not get quite as close.'
print 'Now lets compare the reduced matrix from a and from c:\n'
show(A)
print
show(C)
print '\nWe can see that x4 should be about 1-3(10^(-16))'
print 'However, both algorithms round that to 1 which is not far off.'
print 'Except that in part a this error is multiplied by -10^16 when solving'
print 'for x3 which makes it a much more meaningful error as opposed to part'
print 'c where the error has almost no impact'


