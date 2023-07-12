def secant(f, a, b):

    step = 0
    while abs(f(a)) > 1e-6:

        fa = f(a)
        fb = f(b)

        x_temp = a
        a = a - (a - b) * fa/ (fa - fb)
        b = x_temp 

        step += 1

    return a,step

def f(x):
    return x**3 - 10.0*x**2 + 5.0

print(secant(f,0.0,1.0))

