import numpy as np
import matplotlib.pyplot as plt

A = np.array([2,3])
B=np.array([3,4])

M=(A+B)/2

X=np.array([1,-1])f

if ((X@M))+1 == 0.0:
  print("midpoint between (2,3) and (3,4) satisfy the equation x-y+1=0")
else:
  print("midpoint between (2,3) and (3,4) does not satisfy the equation x-y+1=0")
