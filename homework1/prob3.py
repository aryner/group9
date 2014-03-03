from gauss import *

H = createHilbert(25)
print 'The following is done using a 25x25 Hilbert matrix'

a = rowReduce(H)
a = backSub(a)
print '\na) using basic Gaussian eleminiation we get: '
show(a)
print '\nwith a residual error vector of: '
aError = resErrorVector(H,a)
show(aError)

b = scaledPartialRowReduce(H)
b = backSub(b)
print '\nb) using Gaussian elimination with scaled partial pivoting we get: '
show(b)
print '\nwith a residual error vector of: '
bError = resErrorVector(H,b)
show(bError)

#show(addVectors(aError,scaleVector(bError,-1)))
