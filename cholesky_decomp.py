import numpy as np
import math
import error
def choleski(a,b):
    
    #Decomposition phase
    n = len(a)

    for k in range(n):
    #check if choleski can be used
        try:
            a[k,k] = math.sqrt(a[k,k] - np.dot(a[k,0:k],a[k,0:k]))
        except ValueError:
            error.err('Matrix is not positive definite')
    #operations to transform a into L
        for i in range(k+1,n):
            a[i,k] = (a[i,k] - np.dot(a[i,0:k],a[k,0:k]))/a[k,k]
    for k in range(1,n):
        a[0:k,k] = 0.0
    
    #Solution Phase
    n = len(b)
    # substitution for  [L]{y} = {b}
    for k in range(n):
        b[k] = (b[k] - np.dot(a[k,0:k],b[0:k]))/a[k,k]
    # substitution for [L_transpose]{x} = {y}
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k+1:n,k],b[k+1:n]))/a[k,k]
    return b

a = np.array([[4.0, -2.0, 2.0], [-2.0, 2.0, -4.0], [2.0, -4.0, 11.0]])
b = np.array([3.0, -9.0, -5.0])
b = choleski(a, b)

n = len(b)
for i in range(0, n):
    print(b[i])