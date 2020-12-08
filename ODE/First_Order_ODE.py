import prutorlib as pl
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams
rcParams['figure.figsize'] = 5, 3

def f(y, x): #dy/dx
    
    z = (-30/(1-(x**2))) + ((2*x*y)/(1-(x**2))) - (y**2)
    return z
    
def RK_Method(x, h, y):
    
    K1 = f(y, x)
    K2 = f((y + (0.5*h*K1)), (x + (0.5*h)))
    K3 = f((y + (0.5*h*K2)), (x + (0.5*h)))
    K4 = f((y + (h*K3)), (x + h))
    
    y_new = y + h*(K1 + 2*(K2 + K3) + K4)/6
    x_new = x + h
   
    return (y_new, x_new)

def Euler_Forward(x, h, y):
    
    y_new = y + (h*f(y, x))
    x_new = x + h
    
    return (y_new, x_new)
    
def ODE_Solver(x, x_f, n, y):

    h = (x_f-x)/(n-1)
    
    x1 = x2 = x
    y1 = y2 = y
    
    y1_points = [] 
    y1_points.append(y1)
    y2_points = []
    y2_points.append(y2)
    x_points = []
    x_points.append(x1)
    
    for i in range(n-1):
        
        y1, x1 = RK_Method(x1, h, y1)
        y2, x2 = Euler_Forward(x2, h, y2)
        
        y1_points.append(y1)
        y2_points.append(y2)
        x_points.append(x1)
    
    print(x_points)
    
    plt.plot(x_points, y1_points, label = 'RK4')
    plt.plot(x_points, y2_points, label = 'Euler-Forward')
    plt.legend()
    pl.prutorsaveplot(plt, 'plot2d.pdf')
    
        
x = 0.05
x_f = 0.49
n = 12
y_i = 19.53

ODE_Solver(x, x_f, n, y_i)
