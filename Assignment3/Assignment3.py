import numpy as np
import matplotlib.pyplot as plt
from sympy import *

a, b, c = symbols('a b c')

A = np.array([a,b+c])
B = np.array([a,b-c])
C = np.array([-a,c])
D = np.vstack((A-B,A-C))
Area = abs((D[0][0]*D[1][1]-D[0][1]*D[1][0])/2)

print("Area of the trainagle formed by (a,b+c), (a,b-c) and (-a,c) is ",Area)
