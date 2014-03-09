from gauss import *

matrix = [[1,-1,4,29],[3,-2,-1,-6],[2,-5,6,-55]]

A = gaussSeidel(matrix, [0,0,0], 0.1)
show(A)

