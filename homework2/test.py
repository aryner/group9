from interpolation import *
import numpy as np
import matplotlib.pyplot as plt

x = [1.3, 1.6, 1.9]
fx = [0.6200860, 0.4554022, 0.2818186]
dfx = [-0.5220232, -0.5698959, -0.5811571]

hermiteCo = hermiteCoefficients(x,fx,dfx)
hermite = completeHermite(hermiteCo, x)

print hermite(1.5)

