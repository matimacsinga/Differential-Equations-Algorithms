import numpy as np

def naive_gauss(a, b):
    n = len(b)
    # Elimination Phase
    for col in range(0,n-1):
        for row in range(col+1,n):
            #prevent division by 0
            if a[row,col] != 0.0:
                #compute term to multiply row by
                lam = a[row,col]/a[col,col]
                #compute all values of the row
                a[row,col+1:n] = a[row,col+1:n] - lam*a[col,col+1:n]
                #compute extended part value
                b[row] = b[row] - lam*b[col]
    # Back substitution
    for col in range(n-1,-1,-1):
        b[col] = (b[col] - np.dot(a[col,col+1:n],b[col+1:n]))/a[col,col]
    return b

def pivot_gauss(a,b,tol=1.0e-12):
    n = len(b)
    # Set up scale factors
    s = np.zeros(n)
    #checks max element on each row
    for i in range(n):
        s[i] = max(np.abs(a[i,:]))
    for k in range(0,n-1):
    # Row interchange, if needed
        p = np.argmax(np.abs(a[k:n,k])/s[k:n]) + k
        if abs(a[p,k]) < tol: 
            print('Matrix is singular')
        if p != k:
            #swaps rows of A, B, and scale factors
            b[[p,k]] = b[[k,p]]
            s[[p,k]] = s[[k,p]]
            a[[p,k]] = a[[k,p]]
    # Elimination - same as naive gauss
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
                
    if abs(a[n-1,n-1]) < tol: 
        print('Matrix is singular')
    # Back substitution
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b

if __name__ == "__main__":
    A_1 = np.array([[0.0,1.0,-4.0],
                    [0.0,1.0,0.0,2.0,-1.0],
                    [1.0,2.0,0.0,-2.0,0.0]])
    A_2 = np.array([[0.0,0.0,2.0,1.0,2.0],
                    [0.0,1.0,0.0,2.0,-1.0],
                    [1.0,2.0,0.0,-2.0,0.0],
                    [0.0,0.0,0.0,-1.0,1.0],
                    [0.0,1.0,-1.0,1.0,-1.0]])
    B_1 = np.array([1.0,
                    1.0,
                    -4.0
                    ,-2.0,
                    -1.0])
    B_2 = np.array([1.0,
                    1.0,
                    -4.0
                    ,-2.0,
                    -1.0])
    
    #print(naive_gauss(A_1,B_1))
    print(pivot_gauss(A_2,B_2))