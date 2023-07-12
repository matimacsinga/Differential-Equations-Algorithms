from scipy.misc import derivative
    
def newton_raphson(f, a):

    x = a
    step = 0

    while abs(f(x)) > 1e-3:

        fx = f(x)
        dfx = derivative(f, x, dx = 1e-4)
        x = x - (fx/dfx)

        step += 1

    return x, step

def f(x):
    return x**3 - 10.0*x**2 + 5.0

print(newton_raphson(f,1.0))