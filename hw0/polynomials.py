'''###################################################################
polynomials.py
 homework for math 400
  last worked on: 1/31/14
   represent a polynomail by a list of lists
    where each inner list has 2 elements, a coefficeint
     and an exponent.  The printPoly function requires that
      if there is a constant in the polynomial, it must be the
       last element in the list. The derivative function has the
        same requirement with the additional requirement that if the
         polynomail contians an ax^1 term, it must be the last element
          in the list other than any constants.
'''###################################################################

testP = [[4,512],[7,256],[3,1],[1,0]]

def printPoly(P):
  for i in range(len(P)):
    if P[i][1] > 1 and i < len(P)-1 :
      print("%sx^%s +"%(P[i][0], P[i][1])),
    elif P[i][1] == 1 and i < len(P)-1 :
      print("%sx + "%(P[i][0])),
    elif P[i][1] > 1:
      print("%sx^%s"%(P[i][0], P[i][1])),
    elif P[i][1] == 1:
      print("%sx"%(P[i][0])),
    else:
      print("%s"%(P[i][0])),
  print

def derivative(P):
  D=[]
  for i in range(len(P)):
    D.append([P[i][0]*P[i][1],P[i][1]-1])
    if D[i][1] == 0:
      break
  return D

printPoly(testP)
printPoly(derivative(testP))
printPoly(testP)
