import numpy as np
import swap
import error



def naive_lu(a,b):

    n = len(a)
    #Decomposition phase
    for k in range(0,n-1):
        for i in range(k+1,n):
            #prevent division by 0
            if a[i,k] != 0.0:
              #compute term to multiply row by
              lam = a [i,k]/a[k,k]
              #compute all values of the row
              a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
              #put computed term back in matrix to build lower triangular part
              a[i,k] = lam

    #Solution phase
    #back substitution
    for k in range(1,n):
        b[k] = b[k] - np.dot(a[k,0:k],b[0:k])
    b[n-1] = b[n-1]/a[n-1,n-1]
    #forward substitution
    for k in range(n-2,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b


def pivot_lu(a,b,tol=1.0e-9):

    n = len(a)
    seq = np.array(range(n))
    # set up scale factors
    s = np.zeros((n))
    for i in range(n):
        s[i] = max(abs(a[i,:]))
    
    for k in range(0,n-1):
    # row interchange, if needed
        p = np.argmax(np.abs(a[k:n,k])/s[k:n]) + k
        if abs(a[p,k]) < tol: 
            error.err('Matrix is singular')
        if p != k:
            swap.swapRows(s,k,p)
            swap.swapRows(a,k,p)
            swap.swapRows(seq,k,p)
        # Decomposition phase, same as above
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                a[i,k] = lam

    #Solution phase
    x = b.copy()
    #set up array from scale factors
    for i in range(n):
        x[i] = b[seq[i]]
    #back substitution
    for k in range(1,n):
        x[k] = x[k] - np.dot(a[k,0:k],x[0:k])
    x[n-1] = x[n-1]/a[n-1,n-1]
    #forward substitution
    for k in range(n-2,-1,-1):
        x[k] = (x[k] - np.dot(a[k,k+1:n],x[k+1:n]))/a[k,k]
    return x

if __name__ == "__main__":

    a = np.array([[1.0,2.0,4.0], 
                  [3.0,8.0,14.0], 
                  [2.0,6.0,13.0]])
    b = np.array( [3.0,13.0,4.0])
    #b = naive_lu(a, b)
    b = pivot_lu(a, b)

    n = len(b)
    for i in range(0, n):
        print(b[i])