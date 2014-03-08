from gauss import *

n = 3
H = populateHilbert(n)
#Hi = invertGauss(H)
Hi = invertScaledGauss(H)
show(H)
print
show(Hi)
print
show(matMult(H,Hi))


