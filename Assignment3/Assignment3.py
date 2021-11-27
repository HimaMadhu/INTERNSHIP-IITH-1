import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB


a, b, c = symbols('a b c')
# a, b, c = 1, 2, 3
A = np.array([a,b+c])
B = np.array([a,b-c])
C = np.array([-a,c])
D = np.vstack((A-B,A-C))

Area = abs((D[0][0]*D[1][1]-D[0][1]*D[1][0])/2)
a, b, c = 1, 2, 3
A = np.array([a,b+c])
B = np.array([a,b-c])
C = np.array([-a,c])
D = np.vstack((A-B,A-C))
Area1 = abs((D[0][0]*D[1][1]-D[0][1]*D[1][0])/2)

print("Area of the trainagle formed by (a,b+c), (a,b-c) and (-a,c) is ",Area)
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
print("Area of the trainagle formed by (",a,",",b+c,"), (",a,",",b-c,") and (",-a,",",c,") is ",Area1)
