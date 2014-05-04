'''###################################################################
polynomials.py
 update: 5/3/14
  added stuff deal with polynomials having 2 unknowns
   the derivative and evaluate functions make a lot of
    assumptions.  Those two should only be used if it is
     known that for all terms the degree of one of the
      variables is <= 1 otherwise who knows i haven't even
       tested for that but I know it wont be good

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
test2d = [[[3,2]],[[-1,2]]]
test2d2 = [[[-1,2]],[['3x',2],[-1,0]]]

def add2d(one,two):
  X=[]
  Y=[]
  xD = []
  yD = []
  for i in range(len(one[0])):
    found = False
    if isinstance(one[0][i][0], (int,long,float,complex)):
      for j in range(len(two[0])):
        if isinstance(two[0][j][0], (int,long,float,complex)):
          if one[0][i][1] == two[0][j][1]:
            X.append([one[0][i][0]+two[0][j][0],one[0][i][1]])
            xD.append(j)
            found=True
        else:
          X.append(two[0][j])
          xD.append(j)
      if found==False:
        X.append(one[0][i])
    else:
      X.append(one[0][i])

  for i in range(len(one[1])):
    found = False
    if isinstance(one[1][i][0], (int,long,float,complex)):
      for j in range(len(two[1])):
        if isinstance(two[1][j][0], (int,long,float,complex)):
          if one[1][i][1] == two[1][j][1]:
            Y.append([one[1][i][0]+two[1][j][0],one[1][i][1]])
            yD.append(j)
            found=True
        else:
          Y.append(two[1][j])
          yD.append(j)
      if found==False:
        Y.append(one[1][i])
    else:
      Y.append(one[1][i])

  for i in range(len(xD)):
    del two[0][xD[i]]
  for i in range(len(yD)):
    del two[1][yD[i]]

  for i in range(len(two[1])):
    Y.append(two[1][i])
  for i in range(len(two[0])):
    X.append(two[0][i])
  return [X,Y]



def evaluate2d(P,v):
  sol = 0
  for i in range(len(P[0])):
    if isinstance(P[0][i][0], (int,long,float,complex)):
      sol = sol + P[0][i][0]*v[0]**P[0][i][1]
    else:
      num = float(P[0][i][0][:-1])
      sol = sol + num*v[1]*v[0]**P[0][i][1]
  for i in range(len(P[1])):
    if isinstance(P[1][i][0], (int,long,float,complex)):
      sol = sol + P[1][i][0]*v[1]**P[1][i][1]
    else:
      num = float(P[1][i][0][:-1])
      sol = sol + num*v[0]*v[1]**P[1][i][1]
  return sol

def derivative2dX(P):
  X=[]
  Y=[]
  for i in range(len(P[0])):
    if isinstance(P[0][i][0], (int,long,float,complex)):
      X.append([P[0][i][0]*P[0][i][1],P[0][i][1]-1])
      if P[0][i][1] == 0:
        break
    else:
      num = float(P[0][i][0][:-1])
      X.append([str(num*P[0][i][1])+'y',P[0][i][1]-1])
      if P[1][i][1] == 0:
        break
  for i in range(len(P[1])):
    if isinstance(P[1][i][0], (int,long,float,complex)):
      this = 'stub'
    else:
      Y.append([P[1][i][0][:-1],P[1][i][1]])
  return [X,Y]

def derivative2dY(P):
  X=[]
  Y=[]
  for i in range(len(P[1])):
    if isinstance(P[1][i][0], (int,long,float,complex)):
      Y.append([P[1][i][0]*P[1][i][1],P[1][i][1]-1])
      if P[1][i][1] == 0:
        break
    else:
      num = float(P[1][i][0][:-1])
      Y.append([str(num*P[1][i][1])+'x',P[1][i][1]-1])
      if P[1][i][1] == 0:
        break
  for i in range(len(P[0])):
    if isinstance(P[0][i][0], (int,long,float,complex)):
      this = 'stub'
    else:
      X.append([P[0][i][0][:-1],P[0][i][1]])
  return [X,Y]


def print2d(P):
  for j in range(len(P[0])):
    if P[0][j][1] > 1 and j < len(P[0])-1 :
      print("%sx^%s +"%(P[0][j][0], P[0][j][1])),
    elif P[0][j][1] == 1 and j < len(P[0])-1 :
      print("%sx + "%(P[0][j][0])),
    elif P[0][j][1] > 1:
      print("%sx^%s"%(P[0][j][0], P[0][j][1])),
    elif P[0][j][1] == 1:
      print("%sx"%(P[0][j][0])),
    else:
      print("%s"%(P[0][j][0])),

  for j in range(len(P[1])):
    if P[1][j][1] > 1 and j < len(P[0])-1 :
      print("%sy^%s +"%(P[1][j][0], P[1][j][1])),
    elif P[1][j][1] == 1 and j < len(P[1])-1 :
      print("%sy + "%(P[1][j][0])),
    elif P[1][j][1] > 1:
      print("%sy^%s"%(P[1][j][0], P[1][j][1])),
    elif P[1][j][1] == 1:
      print("%sy"%(P[1][j][0])),
    else:
      print("%s"%(P[1][j][0])),

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

#printPoly(testP)
#printPoly(derivative(testP))
#printPoly(testP)
print2d(test2d)
#print 
#print evaluate2d(test2d,[2,2])
#print2d(derivative2dX(test2d))
#print
#print2d(derivative2dY(test2d))
print
print2d(test2d2)
print 
#print evaluate2d(test2d2,[2,2])
#print2d(derivative2dX(test2d2))
#print
#print2d(derivative2dY(test2d2))
#print
print2d(add2d(test2d,test2d2))
