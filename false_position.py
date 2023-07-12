def false_position(f, a, b):
    
    step = 0
    recursion = b - (f(b) * (a - b))/(f(a) - f(b))
    while abs(f(recursion)) > 1e-6:
        
        if f(a) * f(recursion) < 0:
            b = recursion
        elif f(b) * f(recursion) < 0:
            a = recursion
        elif f(recursion) == 0:
            return recursion 
        recursion = b - (f(b) * (a - b))/(f(a) - f(b))
        step += 1
        
    return recursion, step

def f(x):
    return x**3 - 10.0*x**2 + 5.0

print(false_position(f,0.0,1.0))