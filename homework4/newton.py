import numpy as np
from gauss import *
from polynomials import *

def generateX(numPoints, start, finish):
  return [((finish-start)/(numPoints-1))*i+start for i in range(numPoints)]

def newton2d(eqn1,eqn2, guess):

