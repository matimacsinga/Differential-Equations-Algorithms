def bisection(f, a, b):
    
    step = 0
    recursion = (a + b)/2
    while abs(f(recursion)) > 1e-3:
        
        if f(a) * f(recursion) < 0:
            b = recursion
        elif f(b) * f(recursion) < 0:
            a = recursion
        elif f(recursion) == 0:
            return recursion
        recursion = (a + b)/2
        step += 1
            
    return recursion, step

def f(x):
    return x**3 - 10.0*x**2 + 5.0

print(bisection(f,0.0,1.0))