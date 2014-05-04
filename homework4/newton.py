import numpy as np
from polynomials import *

def generateX(numPoints, start, finish):
  return [((finish-start)/(numPoints-1))*i+start for i in range(numPoints)]

def newton2d(one,two, guess):
  xD1 = derivative2dX(one)
  xD2 = derivative2dX(two)
  yD1 = derivative2dY(one)
  yD2 = derivative2dY(two)

  J1 = [evaluate2d(xD1,guess), evaluate2d(yD1,guess)]
  J2 = [evaluate2d(xD2,guess), evaluate2d(yD2,guess)]

  scalar = 1./(J1[0]*J2[1]-J1[1]*J2[0])

  Jinverse = [[scalar*J2[1],-scalar*J1[1]],
              [-scalar*J2[0],scalar*J1[0]]]

  f1 = evaluate2d(one,guess)
  f2 = evaluate2d(two, guess)

  JIxF1 = Jinverse[0][0]*f1 + Jinverse[0][1]*f2
  JIxF2 = Jinverse[1][0]*f1 + Jinverse[1][1]*f2

  return [guess[0]-JIxF1,guess[1]-JIxF2]

