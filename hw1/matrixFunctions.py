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
    return("write scalarMult()")    


def addVectors(S,T):
    "return S+T"
    return("write addVectors()")


def dot(S,T):
    "return dot product of two vectors"
    return("write dot()")


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
    return("write getCol()")

def transpose(mat):
    "return transpose of mat"
    return("write transpose()")

def getRow(mat, row):
    "return row row from matrix mat"
    return("write getRow()")

def scalarMultMatrix(a,mat):
    "multiply a scalar times a matrix"
    return("write scalarMultMatrix()")


def addMatrices(A,B):
    "add two matrices"
    return("write addMatrics()")


def multiplyMat(mat1,mat2):
    "multiply two matrices"
    return("write multiplyMat()")


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
#testMatrix()
    
