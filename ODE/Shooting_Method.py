import prutorlib as pl
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams
rcParams['figure.figsize'] = 5, 3

def v_(L, u, v, x):
    
    z = #Function for Y'' in Y' and Y
    
    return float(z)

def F(y, x): #Return f
    
    u = y[0]
    v = y[1]
    
    f = np.zeros((2,1))
    f[0] = v
    f[1] = v_(L, u, v, x)
    
    return f

def RK_Method(x, h, y, f):
    
    K0 = F(y, x)
    
    y_ = y + (0.5*h*K0) #2nd Order R-K
    x_ = x + (0.5*h) #2nd Order R-K
    K1 = F(y_, x_)
    
    y_new = y + (h*K1)
    x_new = x + h
    
    return (y_new, x_new)

def Secant_Method(v1, v2, b, u11, u12):
    
    v3 = v2 - ((u12-b)*(v2-v1)/(u12-u11))
    return v3
    
def Shooting_Method(x, x_f, h, a, b, v1, v2, e, i_max):

    i = 0
    err = 1
    
    while err >= e:
        
        x_i = x #starting_x
        
        y = np.zeros((2,1))
        y[0] = a
        y[1] = v1
        
        while (x < x_f):
        
            f = F(y, x)
            y, x = RK_Method(x, h, y, f)
        
        u11 = y[0] #value_at_boundary_using_v1
        
        x = x_i
        y = np.zeros((2,1))
        y[0] = a
        y[1] = v2

        y_points = []
        y_points.append(a)
        x_points = []
        x_points.append(x)
        
        while (x < L):
            
            f = F(y, x)
            y, x = RK_Method(x, h, y, f)
            
            x_points.append(x)
            y_points.append(y[0])
        
        u12 = y[0]  #value_at_boundary_using_v2
        
        v3 = Secant_Method(v1, v2, b, u11, u12)
        v1, v2 = v2, v3
        
        
        err = abs(u12-b) 
        i = i+1
        x = x_i
        
        if i > i_max :
            print('ERROR: Limit Exceeded')
            return None
        
    print('The solution was obtained after', i, 'iterations')
        
    plt.plot(x_points, y_points)
    pl.prutorsaveplot(plt, 'plot2d.pdf')
    
    return None

L = 4.0
x_initial = 0.0
x_final = 4.0
h = 0.1
a = 0.0 #y_initial
b = 0.0 #y_final
v1 = 0.0 #firstguess
v2 = 2.0 #secondguess
e = 0.0001 #tolerance
i_max = 20

Shooting_Method(x_initial, x_final, h, a, b, v1, v2, e, i_max)

#shooting method with 2nd order R-K method
        
    
    
