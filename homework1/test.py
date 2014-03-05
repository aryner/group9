from gauss import *

A = [[1,1,0,3],
     [2,1,-1,1],
     [3,-1,-1,2],
     [-1,2,3,-1]]
b = [4,0,1,1]
c = [4,-7,13,-13]

L,U = LU(A)
show(L)
print
show(U)
y = forwardSub(augment(L,b))
print
show(y)
x = backSub(augment(U,y))
print
show(x)
print
show(checkSol_1(augment(A,b),x))
print
a = rowReduce(augment(A,b))
a = backSub(a)
show(checkSol_1(augment(A,b),a))

