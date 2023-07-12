import math
from numpy import sign

def ridder(f,a,b,tol=1.0e-3):

    f1 = f(a)
    if f1 == 0.0:
        return a
    
    f2 = f(b)
    if f2 == 0.0:
        return b
    
    if sign(f1) == sign(f2):
        return None

    x3 = 0.5 * (a + b)
    f3 = f(x3)
    fa = f(a)

    if fa == 0.0:
        return a
    
    fb = f(b)
    if fb == 0.0:
        return b
    
    if sign(f2)!= sign(f3):
        x1 = x3
        f1 = f3

    for i in range(30):
        
        c = 0.5*(a + b)
        fc = f(c)
        s = math.sqrt(fc**2 - fa*fb)
        if s == 0.0:
            return None
        
        dx = (c - a)*fc/s
        if (fa - fb) < 0.0:
            dx = -dx
        x = c + dx
        fx = f(x)
        
        if i > 0:
            if abs(x - x_old) < tol*max(abs(x),1.0):
                return x, i
        x_old = x
        
        if sign(fc) == sign(fx):

            if sign(fa)!= sign(fx):

                b = x
                fb = fx
            else:

                a = x
                fa = fx
        else:

            a = c
            b = x
            fa = fc
            fb = fx

    return None

def f(x):
    return x**3 - 10.0*x**2 + 5.0

print(ridder(f,0.0,1.0))