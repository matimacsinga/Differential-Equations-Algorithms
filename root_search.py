from numpy import sign

def root_search(f,a,b,dx):

    x1 = a; 
    f1 = f(a)
    x2 = a + dx; 
    f2 = f(x2)

    while sign(f1) == sign(f2):

        if x1 >= b: 
            return None,None
        x1 = x2; 
        f1 = f2
        x2 = x1 + dx; 
        f2 = f(x2)

    return x1,x2

def f(x): 
    return x**3 - 10.0*x**2 + 5.0

x1 = 0.0; 
x2 = 1.0

for i in range(4):
    dx = (x2 - x1)/10.0
    x1,x2 = root_search(f,x1,x2,dx)

x = (x1 + x2)/2.0
print(f"Root = {x}")
