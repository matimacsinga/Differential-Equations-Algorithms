from numpy import sign
import math
from scipy.misc import derivative

def brent(f,a,b,tol=1.0e-1):

    fa = f(a)
    if fa == 0.0:
        return a
    
    fb = f(b)
    if fb == 0.0:
        return b
    
    if sign(fa) == sign(fb):
        return None

    x = 0.5*(a + b)
    
    for i in range(30):
        fx = f(x)
        if fx == 0.0:
            return x
        
        if sign(fa) != sign(fx):
            b = x
        else:
            a = x
        
        dfx = derivative(f,x,dx = 1e-6)
        
        try:
            dx = -fx/dfx
        except ZeroDivisionError:
            dx = b - a
        x = x + dx
        
        if (b - x)*(x - a) < 0.0:
            dx = 0.5*(b - a)
            x = a + dx
       
        if abs(dx) < tol*max(abs(b),1.0):
            return x,i
    
    return None

def f(x): 
    return x**3 - 10.0*x**2 + 5.0

a = 0.0
b = 1.0
print(brent(f,a,b,tol=1.0e-2))