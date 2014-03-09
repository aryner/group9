from gauss import *

n = [3,5,7,8,10,15,20,25]
print 'We will compare the exact inverse of Hilbert matrices of different'
print 'sizes with approximate inverses found with basic Gaussian elemination'
print 'and partialy scaled Gaussian elemination by subtracting each element'
print 'in the approximation from each element in the exact inverse. The closer'
print 'the resulting matrix is to the zero matrix, better the approximation was.'
print 'Because these matrices are hard to fit on the screen, instead of showing'
print 'them we will sum the absolute value of each element in the compare matrix'
print 'and divide by the number of elements in the matrix to get an average element'
print 'error. We will also show the result of multiplying the approximations with the'
print 'Hilbert matrix to see how close to the identy matrix we get. Again '
print 'Because it is hard to read these matrices on the screen we will print'
print 'the average element error from the identy matrix rather than the matrix'

for i in n:
  H = populateHilbert(i)
  I = hilbertInverse(i)
  Hb = invertGauss(H)
  Hs = invertScaledGauss(H)
  print '\n\t\tFor size %s'%i
  avgE = avgElement(compareMats(I,Hb))
  avgI = avgElement(compareMats(matMult(H,Hb), createIdentity(i)))
  print 'For basic Gaussian elemination the average element error is: %s'%avgE
  print 'And the approximation times the Hilbert matrix is: %s\n'%avgI

  avgE = avgElement(compareMats(I,Hs))
  avgI = avgElement(compareMats(matMult(H,Hs), createIdentity(i)))
  print 'For partially scaled Gaussian elemination the average element error is: %s'%avgE
  print 'And the approximation times the Hilbert matrix is: %s\n'%avgI

print 'All the way up to size 7 the average element error is pretty small but as soon'
print 'as we reach size 8, both approximations have huge jumps in their error that keep'
print 'getting bigger.  By 25 they are HUGE. What is particularly interesting is that'
print 'the difference between the identity matrix and the multiple of the approximation'
print 'and the Hilbert matrix never gets that big.  Under size 15 it seems pretty close.'
print 'Even at size 25, the error is much bigger than what is acceptable but compared to'
print 'the erros in the approximations themselves, they are nothing'
