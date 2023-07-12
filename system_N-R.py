import numpy as np
import math

def swap_rows(v, i, j):

    if len(v.shape) == 1:
        v[i], v[j] = v[j], v[i]
    else:
        v[[i, j], :] = v[[j, i], :]


def pivot_gauss(a, b, tol=1.0e-12):

    n = len(b)
    s = np.zeros(n)

    for i in range(n):
        s[i] = max(np.abs(a[i, :]))

    for k in range(0, n - 1):
        
        p = np.argmax(np.abs(a[k:n, k]) / s[k:n]) + k
        if abs(a[p, k]) < tol:
            print("singular")
        if p != k:
            swap_rows(b, k, p)
            swap_rows(s, k, p)
            swap_rows(a, k, p)
        
        for i in range(k + 1, n):
            if a[i, k] != 0.0:
                lam = a[i, k] / a[k, k]
                a[i, k + 1:n] = a[i, k + 1:n] - lam * a[k, k + 1:n]
                b[i] = b[i] - lam * b[k]

    if abs(a[n - 1, n - 1]) < tol:
        print("singular")
    
    b[n - 1] = b[n - 1] / a[n - 1, n - 1]

    for k in range(n - 2, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k + 1:n], b[k + 1:n])) / a[k, k]

    return b

def jacobian(f,x):

    h = 1.0e-4
    n = len(x)
    jac = np.zeros((n,n))
    f0 = f(x)

    for i in range(n):
        temp = x[i]
        x[i] = temp + h
        f1 = f(x)
        x[i] = temp
        jac[:,i] = (f1 - f0)/h

    return jac,f0

def newton_raphson2(f,x,tol=1.0e-9):

    for i in range(30):

        jac,f0 = jacobian(f,x)
        if math.sqrt(np.dot(f0,f0)/len(x)) < tol:
            return x
        dx = pivot_gauss(jac,-f0)
        x = x + dx
        if math.sqrt(np.dot(dx,dx)) < tol*max(max(abs(x)),1.0):
            return x

def f(x):

    f = np.zeros(len(x))
    f[0] = math.sin(x[0]) + x[1]**2 + math.log(x[2]) - 7.0
    f[1] = 3.0*x[0] + 2.0**x[1] - x[2]**3 + 1.0
    f[2] = x[0] + x[1] + x[2] - 5.0
    return f

x = np.array([1.0, 1.0, 1.0])
print(newtonRaphson2(f,x))
