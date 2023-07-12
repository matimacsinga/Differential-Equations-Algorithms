import numpy as np

def swapRows(v, i, j):
    if len(v.shape) == 1:
        v[i], v[j] = v[j], v[i]
    else:
        v[[i, j], :] = v[[j, i], :]

def LUdecomp(a, seq, tol=1.0e-9):
    # Set up scale factors
    n = len(a)
    s = np.zeros((n))
    for i in range(n):
        s[i] = max(abs(a[i, :]))
    for k in range(0, n - 1):
    # Row interchange, if needed
        p = np.argmax(np.abs(a[k:n, k]) / s[k:n]) + k
        if abs(a[p, k]) < tol: print("Matrix is singular")
        if p != k:
            swapRows(s, k, p)
            swapRows(a, k, p)
            swapRows(seq, k, p)
        for i in range(k + 1, n):
         if a[i, k] != 0.0:
            lam = a[i, k] / a[k, k]
            a[i, k + 1:n] = a[i, k + 1:n] - lam * a[k, k + 1:n]
            a[i, k] = lam
    return a, seq

def LUsolve(a,b,seq):
    n = len(a)
    # Rearrange constant vector; store it in [x]
    x = b.copy()
    for i in range(n):
        x[i] = b[seq[i]]
    # Solution
    for k in range(1,n):
         x[k] = x[k] - np.dot(a[k,0:k],x[0:k])
    x[n-1] = x[n-1]/a[n-1,n-1]
    for k in range(n-2,-1,-1):
        x[k] = (x[k] - np.dot(a[k,k+1:n],x[k+1:n]))/a[k,k]
    return x

def matInv(a):
    n = len(a[0])
    inverse = np.identity(n)
    seq = np.array(range(n))
    a, seq = LUdecomp(a, seq)
    for i in range(n):
        inverse[:, i] = LUsolve(a, inverse[:, i], seq)
    return inverse


a = np.array([[ 1.0,0.5,0.25,0.125],
              [0.0,1.0,0.33,0.11],
              [ 0.0,0.0,1.0,0.25],
              [0.0,0.0,0.0,1.0]])
aOrig = a.copy()
aInv = matInv(a)
print("\naInv =\n",aInv)
print("\nCheck: a*aInv =\n", np.dot(aOrig,aInv))
input("\nPress return to exit")
