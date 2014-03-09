from gauss import *

nums = [3,5,10,15,20,25]

H = [populateHilbert(i) for i in nums]
Vb = [bHilbert(i) for i in nums]
Hb = [augment(H[i],Vb[i]) for i in range(len(nums))]

a = [rowReduce(Hb[i]) for i in range(len(nums))]
A = [backSub(a[i]) for i in range(len(nums))]
Ar = [resErrorVector(Hb[i],A[i]) for i in range(len(nums))]

b = [scaledPartialRowReduce(Hb[i]) for i in range(len(nums))]
B = [backSub(b[i]) for i in range(len(nums))]
Br = [resErrorVector(Hb[i],B[i]) for i in range(len(nums))]

L = [L(H[i]) for i in range(len(nums))]
U = [U(H[i]) for i in range(len(nums))]
y = [forwardSub(augment(L[i],Vb[i])) for i in range(len(nums))]
x = [backSub(augment(U[i],y[i])) for i in range(len(nums))]
xr = [resErrorVector(Hb[i],x[i]) for i in range(len(nums))]

g = [gaussSeidel(Hb[i], [0 for j in range(nums[i])],0.1) for i in range(len(nums))]
gr = [resErrorVector(Hb[i],g[i]) for i in range(len(nums))]

print 'Here we made 6 Hilbert matrices of sizes 3,5,10,15,20,25 and'
print 'solved them each using basic Gaussian elimination, '
print 'scaled partial pivoting, LU factorization, and Gauss-Seidel.'
print 'Below are the residual error vectors for each matrix size and'
print 'solution method combination:'
print
for i in range(len(nums)):
  print '\t\t\t\t\t\t\tsize: %d'%nums[i]
  print '\tbasic\t\t\t\tscaled\t\t\t\tLU\t\t\t\tG-S'
  for j in range(len(Ar[i])):
    print '%s\t\t%s\t\t%s\t\t%s'%(Ar[i][j],Br[i][j],xr[i][j],gr[i][j])
  print

print '\nIt seems that throughout basic, scaled, and LU give consistently'
print 'not great answers.  Most elements in these vectors fall between'
print 'about -4 and 4 with a few going higher, some almost reaching 10'
print 'or -10.  Gauss-Seidel on the other hand is very consistently close'
print 'to the solution with the elements in its error vectors never leaving'
print 'a lower bound of -0.03 and upper bound of 0.6'
