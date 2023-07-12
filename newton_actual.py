import numpy as np
import math


def newton(x, y, ip):

    n = len(y) - 1 
    p = x[n]

    for k in range(1, n + 1):
        p = x[n - k] + (ip - y[n - k]) * p

    return p


def coeffts(x, y):

    m = len(x) 
    a = y.copy()

    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1]) / (x[k:m] - x[k - 1])

    return a

x_array = np.array([-3.0,2.0,-1.0,3.0])
y_array = np.array([0.0,5.0,-4.0,12.0])
a = coeffts(x_array, y_array)
interpolation_point = 1.0
print(newton(a,x_array,interpolation_point))


