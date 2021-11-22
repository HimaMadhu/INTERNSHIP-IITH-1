import numpy as np
import matplotlib.pyplot as plt

A = np.array([1,-2])
B=np.array([-3,4])

T1=(A+2*B)/3
T2=(2*A+B)/3

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

x_AB = line_gen(A,B)
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
# round(float(S[j]),2)

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.7), A[1] * (1 - 0.05) , 'A({}, {})'.format(A[0], A[1]))
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.04), B[1] * (1- 0.02) , 'B({}, {})'.format(B[0], B[1]))
plt.plot(T1[0], T1[1], 'o')
plt.text(T1[0] * (1 - 0.1), T1[1] , 'T₁({}, {})'.format(round(T1[0],2),T1[1]))
plt.plot(T2[0], T2[1], 'o')
plt.text(T2[0] * (1- 0.1), T2[1], 'T₂({}, {})'.format(round(T2[0],2),T2[1]))
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
# plt.axis('equal')

plt.show()
