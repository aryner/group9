from newton import *
import numpy as np
import matplotlib.pyplot as plt

eqn1 = [[[3,2]],[[-1,2]]]
eqn2 = [[[-1,2]],[['3x',2],[-1,0]]]

test1 = [[[2,2]],[[1,2],[-8,0]]]
test2 = [[[1,2],[-4,0]],[[-1,2],['1x',1]]]

print newton2d(test1,test2,[1,1])
