import prutorlib as pl
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams
rcParams['figure.figsize'] = 5, 3

def H(y, z, t):  #dy/dt
    
    h = ((-y+z)*np.exp(1-t)) + (0.5*y)
    return h

def G(y, z, t): #dz/dt
    
    g = y - (z**2)
    return g
    
def F(w, t):
    
    f = np.zeros((2,1))
    
    y = w[0]
    z = w[1]
    
    f[0] = H(y, z, t)
    f[1] = G(y, z, t)
    
    return f
    

def RK_Method(t, h, w, f): #4th order R-K
    
    K1 = F(w, t)
    K2 = F((w + (0.5*h*K1)), (t + (0.5*h)))
    K3 = F((w + (0.5*h*K2)), (t + (0.5*h)))
    K4 = F((w + (h*K3)), (t + h))
    
    w_new = w + h*(K1 + 2*(K2 + K3) + K4)/6
    t_new = t + h
   
    return (w_new, t_new)

    
def System_of_ODE(t, t_f, h, y_i, z_i):

    w = np.zeros((2,1))
    w[0] = y_i
    w[1] = z_i

    f = F(w, t)
    
    y_points = [] 
    y_points.append(y_i)
    z_points = []
    z_points.append(z_i)
    t_points = []
    t_points.append(t)
    
    while t < t_f:
        
        w, t = RK_Method(t, h, w, f)
        y_points.append(w[0])
        z_points.append(w[1])
        t_points.append(t)
        
    print('Plotting Y v/s T and Z v/s T')
    plt.plot(t_points, y_points)
    plt.plot(t_points, z_points)
    pl.prutorsaveplot(plt, 'plot2d.pdf')
    
        
t = 0
t_f = 1
h = 0.1
y_i = 3
z_i = 0.2

System_of_ODE(t, t_f, h, y_i, z_i)
