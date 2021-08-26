import math
import numpy as np
e = math.e
pi = math.pi
#Realizado por: Natalia Gaona Salamanca
def newton_raphson(f, df, x, TOL):
    error = 1
    iterations = 0
    while error > TOL:
        new_x = x - f(x)/df(x)
        error = abs(new_x - x)
        x = new_x
        iterations += 1
        print(f'x{iterations}: {x}')
    print(f"Newton's Estimate = {x:.15f}\nIterations: {iterations}")

def modified_newton(f, df, ddf, x, TOL):
    error = 1
    iterations = 0
    while error > TOL:
        f_x = f(x)
        d_x = df(x)
        new_x = x - (f_x*d_x)/(d_x*d_x - f_x*ddf(x))
        error = abs(new_x - x)
        x = new_x
        iterations += 1
        print(f'x{iterations}: {x}')
    print(f"Modified Newton Estimate = {x:.15f}\nIterations: {iterations}")


if __name__ == '__main__':
    f = lambda x: np.exp(x)-x-1
    df = lambda x: np.exp(x)-1
    ddf = lambda x: np.exp(x)
    newton_raphson(f, df, 1, 1e-5)
    modified_newton(f, df, ddf, 1, 1e-5)