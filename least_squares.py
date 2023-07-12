import numpy as np
import math
import matplotlib.pyplot as plt

def swap_rows(v, i, j):

    if len(v.shape) == 1:
        v[i], v[j] = v[j], v[i]
    else:
        v[[i, j], :] = v[[j, i], :]


def gaussPivot(a, b, tol=1.0e-12):

    n = len(b)
    
    s = np.zeros(n)

    for i in range(n):

        s[i] = max(np.abs(a[i, :]))

    for k in range(0, n - 1):
        
        p = np.argmax(np.abs(a[k:n, k]) / s[k:n]) + k

        if abs(a[p, k]) < tol:
            print('singular')
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


def polynomial_fit(x,y,m):

    a = np.zeros((m+1,m+1))
    b = np.zeros(m+1)
    s = np.zeros(2*m+1)

    for i in range(len(x)):

        temp = y[i]
        for j in range(m+1):
            b[j] = b[j] + temp
            temp = temp*x[i]

        temp = 1.0
        for j in range(2*m+1):
            s[j] = s[j] + temp
            temp = temp*x[i]

    for i in range(m+1):
        for j in range(m+1):
            a[i, j] = s[i + j]
        
    return gaussPivot(a, b)

def eval_polynomial(c,x):

    m = len(c) - 1
    p = c[m]

    for j in range(m):
        p = p*x + c[m-j-1]

    return p

def standard_deviation(c,x,y):

    n = len(x) - 1
    m = len(c) - 1
    sigma = 0.0

    for i in range(n+1):
        p = eval_polynomial(c,x[i])
        sigma = sigma + (y[i] - p)**2

    sigma = math.sqrt(sigma/(n - m))
    return sigma

x = np.array([-0.04,0.93,1.95,2.90,3.83,5.0, 5.98,7.05,8.21,9.08,10.09])
y = np.array([-8.66,-6.44,-4.36,-3.27,-0.88,0.87, 3.31,4.63,6.19,7.4,8.85])

while True:
    try:
        m = eval(input("\nDegree of polynomial ==> "))
        # Returns coefficients of the polynomial p(x) = c[0] + c[1]x + c[2]xˆ2 +...+ c[m]xˆm
        # that fits the specified data in the least squares sense.
        coeff = polyFit(x,y,m)
        print("Coefficients are:\n",coeff)
        # Computes the std. deviation between p(x) and the data.
        print("Std. deviation =",stdDev(coeff,x,y))
    except SyntaxError: break
input("Finished. Press return to exit")