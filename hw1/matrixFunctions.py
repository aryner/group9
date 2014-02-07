"""
matrixFunctions.py

2/6/14  bic M400

This is a skeleton for the matrix part of first Math 400 assignment

"""

#######  START Administrivia 
m400group = 9   # change this to your group number

m400names = ['alex ryner', 'jared halpert', 'michael sims', 'kason soohoo'] # change this for your names

def printNames():
  print("matrixFunctions.py for group %s:"%(m400group)),
  for name in m400names:
    print("%s, "%(name)),
  print

printNames()

#######  END Administrivia


"""
Vector Functions

copy these three functions from your finished vectorFunctions.py file

"""

def scalarMult(s,V):
  "return vector sV"
  return [k*s for k in V]   


def addVectors(S,T):
  "return S+T"
  result = range(len(S))
  for i in range(len(S)):
    result[i] = S[i] + T[i]
  return result


def dot(S,T):
  "return dot product of two vectors"
  temp = range(len(S))
  for i in range(len(S)):
    temp[i] = S[i] * T[i]
  result = 0
  for i in range(len(S)):
    result += temp[i]
  return result


"""

Matrix Functions

"""



def showMatrix(mat):
  "Print out matrix"
  for row in mat:
    print(row)


def rows(mat):
  "return number of rows"
  return(len(mat))

def cols(mat):
  "return number of cols"
  return(len(mat[0]))
 

#### Functions for you to finish

def getCol(mat, col):
  "return column col from matrix mat"
  result = range(len(mat))
  for i in result:
    result[i] = mat[i][col]
  return result

def transpose(mat):
  "return transpose of mat"
  result = range(len(mat[0]))
  for i in result:
    result[i] = getCol(mat,i)
  return result

def getRow(mat, row):
  "return row row from matrix mat"
  return mat[row]

def scalarMultMatrix(a,mat):
  "multiply a scalar times a matrix"
  return [scalarMult(a,k) for k in mat]


def addMatrices(A,B):
  "add two matrices"
  result = range(len(A))
  for i in result:
    result[i] = addVectors(A[i],B[i])
  return result


def multiplyMat(mat1,mat2):
  "multiply two matrices"
  result = range(len(mat1))
  for i in result:
    result[i] = [dot(getRow(mat1,i),getCol(mat2,k)) for k in range(len(mat2[0]))]
  return result


######  Initial tests

A= [[4,-2,1,11],
  [-2,4,-2,-16],
  [1,-2,4,17]]

Ae= [[4,-2,1],
  [-2,4,-2],
  [1,-2,4]]


Bv=[11,-16,17]

Bm=[[11,-16,17]]

C=[2,3,5]

print("running matrixFunction.py file")

def testMatrix():
  print("A")
  showMatrix(A)
  print("Bm")
  showMatrix(Bm)
  print("Ae")
  showMatrix(Ae)
  print("multiplyMat(Ae,A)")
  showMatrix(multiplyMat(Ae,A))
  print("scalarMultMatrix(2,A))")
  showMatrix(scalarMultMatrix(2,A))
  print("addMatrices(A,A)")
  showMatrix(addMatrices(A,A))
  print("transpose(A)")
  showMatrix(transpose(A))

###  uncomment next line to run initial tests 
testMatrix()
  
