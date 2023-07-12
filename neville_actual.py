import numpy as np
import matplotlib.pyplot as plt


def neville(x, y, ip):

    n = len(x) 
    for k in range(1, n):
        y[0:n - k] = ((ip - x[k:n]) * y[0:n - k]
                       + (x[0:n - k] - ip) * y[1:n - k + 1]) / (x[0:n - k] - x[k:n])

    return y[0]


def rational(xData, yData, x):
    m = len(xData)
    r = yData.copy()
    rOld = np.zeros(m)
    for k in range(m - 1):
        for i in range(m - k - 1):
            if abs(x - xData[i + k + 1]) < 1.0e-9:
                return yData[i + k + 1]
            else:
                c1 = r[i + 1] - r[i]
                c2 = r[i + 1] - rOld[i + 1]
                c3 = (x - xData[i]) / (x - xData[i + k + 1])
                r[i] = r[i + 1] + c1 / (c3 * (1.0 - c1 / c2) - 1.0)
                rOld[i + 1] = r[i + 1]
    return r[0]


x_array = np.array([-3.0,2.0,-1.0,3.0])
y_array = np.array([0.0,5.0,-4.0,12.0])
interpolation_point = 1.0
print(neville(x_array,y_array,interpolation_point))

