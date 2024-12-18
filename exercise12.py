import numpy as np

M = np.array([3,2,1,4]).reshape(2, 2)


M_inv = np.linalg.inv(M)

print(M_inv)

I =np.matmul(M_inv, M)

print(I)

A = np.array([7,5,-3,3,-5,2,5,3,-7]).reshape(3,3)

print(A)

r= np.array([16,-8,0]).reshape(3, 1)

print(r)

A_inv = np.linalg.inv(A)

b=np.matmul(A_inv, r)

print(b)