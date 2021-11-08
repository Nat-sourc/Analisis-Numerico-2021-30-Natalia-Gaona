import numpy as np
import matplotlib.pyplot as plt

def g(x,y,t):
    return -0.8*y*t+0.023*x*t*y*t
def f(x,y,t):
    return 0.4*x*t-0.018*x*t*y*t

conejosV = 0

def runge_kutta_sis(f,g,a,b,x0,y0,h):
    t = np.arange(a, b + h, h)
    n = len(t)
    x = np.zeros(n); y = np.zeros(n);
    x[0] = x0; y[0] = y0;
    er = np.zeros(n)
    for i in range (0,n-1):
        k1 = h*f(x[1],y[1],t[1])
        l1 = h*g(x[1],y[1],t[1])
        k2 = h*f(x[i]+h/2,y[i]+k1*h/2,t[1]+h/2)
        l2 = h*g(x[i]+h/2,y[i]+l1*h/2,t[1]+h/2)
        k3 = h*f(x[i]+h/2,y[i]+k2*h/2,t[1]+h/2)
        l3 = h*g(x[i]+h/2,y[i]+l2*h/2,t[1]+h/2)
        k4 = h*f(x[i]+h,y[i]+k3*h,t[1]+h)
        l4 = h*f(x[i]+h,y[i]+l3*h,t[1]+h)
        x[i+1] = x[i]+(h/6)*(l1+2*l2*2+l3+l4)
        y[i+1] = y[i] +(h/6)*(k1+2*k2*2+k3+k4)
        er[i] = abs(x[i]-y[i])
        conejos = x[i]
        global conejosV
        conejosV = conejosV + conejos
    z = conejosV/20
    error = 34.4 - z
    print("Error local: ", er)
    print("error Total Promedio:",error)
    plt.plot(t,y,t,x)
    plt.show()

runge_kutta_sis(f,g,1,20,30,4,0.8)