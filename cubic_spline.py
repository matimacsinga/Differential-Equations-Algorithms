import numpy as np

def lu(c, d, e, b):

    n = len(d)
    for k in range(1, n):

        lam = c[k - 1] / d[k - 1]
        d[k] = d[k] - lam * e[k - 1]
        c[k - 1] = lam

    for k in range(1, n):
        b[k] = b[k] - c[k - 1] * b[k - 1]

    b[n - 1] = b[n - 1] / d[n - 1]

    for k in range(n - 2, -1, -1):
        b[k] = (b[k] - e[k] * b[k + 1]) / d[k]

    return b


def curvatures(x, y):
    
    n = len(x) - 1
    c = np.zeros(n)
    d = np.ones(n + 1)
    e = np.zeros(n)
    k = np.zeros(n + 1)

    c[0:n - 1] = x[0:n - 1] - x[1:n]
    d[1:n] = 2.0 * (x[0:n - 1] - x[2:n + 1])
    e[1:n] = x[1:n] - x[2:n + 1]
    k[1:n] = 6.0 * (y[0:n - 1] - y[1:n]) / (x[0:n - 1] - x[1:n]) - 6.0 * (
                y[1:n] - y[2:n + 1]) / (x[1:n] - x[2:n + 1])
    
    lu(c,d,e,k)
    return k

def find_seg(data, x):
        
        left_bound = 0
        right_bound = len(data) - 1

        while 1:

            if (right_bound - left_bound) <= 1:
                return left_bound
            
            i = (left_bound + right_bound) // 2

            if x < data[i]:
                right_bound = i
            else:
                left_bound = i

def spline(x, y, k, ip):

    i = find_seg(x, ip)
    h = x[i] - x[i + 1]
    y = ((ip - x[i + 1]) ** 3 / h - (ip - x[i + 1]) * h) * k[i] / 6.0 - ((ip - x[i]) ** 3 / h - (ip - x[i]) * h) * k[i + 1] / 6.0 \
        + (y[i] * (ip - x[i + 1]) - y[i + 1] * (ip - x[i])) / h
    
    return y


# Exemple 3.9 page 125

x = np.array([1, 2, 3, 4, 5], float)
y = np.array([0, 1, 0, 1, 0], float)
# Returns the curvatures of cubic spline at its knots.
k = curvatures(x, y)
while True:
    try:
        x = eval(input("\nx ==> "))
    except SyntaxError: break
    # Evaluates cubic spline at x. The curvatures k can be
    # computed with the function ’curvatures’.
    print("y =", evalSpline(x, y, k, x))

input("Done. Press return to exit")