from gauss import *

n = 5
H = populateHilbert(n)
bv = bHilbert(n)
Hb = augment(H,bv)
print "The following is done using a %ix%i Hilbert matrix shown here:" %(n,n)
show(Hb)

a = rowReduce(Hb)
a = backSub(a)
print '\na) using basic Gaussian eleminiation we get: '
show(a)
#print '\nwith a residual error vector of: '
#aError = resErrorVector(Hb,a)
#show(aError)

b = scaledPartialRowReduce(Hb)
b = backSub(b)
print '\nb) using Gaussian elimination with scaled partial pivoting we get: '
show(b)
#print '\nwith a residual error vector of: '
#bError = resErrorVector(Hb,b)
#show(bError)

L,U = LU(H)
y = forwardSub(augment(L,bv))
x = backSub(augment(U,y))
print '\nc) using LU factorization we get:'
show(x)
#print '\nwith a residual error vector of: '
#bError = resErrorVector(Hb,x)
#show(bError)

