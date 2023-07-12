import numpy as np
from lu_decomp import *

def matInv(a):
    n = len(a[0])
    aInv = np.identity(n)
    for i in range(n):
        aInv[:,i] = pivot_lu(a,aInv[:,i])
    return aInv

a = np.array([[ 1.0,0.5,0.25,0.125],
              [0.0,1.0,0.33,0.11],
              [ 0.0,0.0,1.0,0.25],
              [0.0,0.0,0.0,1.0]])
aOrig = a.copy()
aInv = matInv(a)
print("\naInv =\n",aInv)
print("\nCheck: a*aInv =\n", np.dot(aOrig,aInv))
input("\nPress return to exit")