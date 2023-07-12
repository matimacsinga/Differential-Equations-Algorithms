import numpy as np
import math

def neville(x, y, ip):

    y_final = 0

    n = len(x)

    for i in range(n):
        
        p = 1
        
        for j in range(n):

            if i != j:
                p = p * (ip - x[j])/(x[i] - x[j])
        
        y_final = y_final + p * y[i]    

    return y_final

def lagrange(x, y, ip):

    y_final = 0

    n = len(x)

    for i in range(n):
        
        p = 1
        
        for j in range(n):

            if i != j:
                p = p * (ip - x[j])/(x[i] - x[j])
        
        y_final = y_final + p * y[i]    

    return y_final

def newton(x, y, ip):

    y_final = 0

    n = len(x)

    for i in range(n):
        
        p = 1
        
        for j in range(n):

            if i != j:
                p = p * (ip - x[j])/(x[i] - x[j])
        
        y_final = y_final + p * y[i]    

    return y_final

x_array = np.array([-3.0,2.0,-1.0,3.0])
y_array = np.array([0.0,5.0,-4.0,12.0])
interpolation_point = 1.0
print(lagrange(x_array, y_array, interpolation_point))

