import prutorlib as pl
from mpl_toolkits import mplot3d
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import linalg as LA
import math
from pylab import rcParams

def U(x, t):
    
    return float(np.exp(-(np.pi)*(np.pi)*t)*np.sin(np.pi*x))

def Plots(x, u, ue, t, errmax, phi):
    
    rcParams['figure.figsize'] = 5, 3
    
    plt.figure()
    plt.plot(x,u, '+r',label = r'FTCS solution') 
    plt.plot(x,ue, label = r'Analytic solution') 
    plt.xlabel(r'distance', fontsize=10)
    plt.ylabel(r'function', fontsize=10)
    pl.prutorsaveplot(plt, 'plot1.pdf')
    
    plt.figure()
    plt.plot(t,errmax) 
    plt.xlabel(r'time', fontsize=10)
    plt.ylabel(r'maxerror', fontsize=10)
    pl.prutorsaveplot(plt, 'plot2.pdf')
    
    dist, time = np.meshgrid(x, t) # no idea why to do that
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(dist, time, np.transpose(phi),cmap=cm.jet, linewidth=0.1)
    pl.prutorsaveplot(plt, 'plot3.pdf')


def FTCS(a, L, T, Nx, Nt):
    
    x = np.linspace(0, L, Nx+1)
    t = np.linspace(0, T, Nt+1)
    
    dx = x[1] - x[0]
    dt = t[1] - t[0]
    
    F = a*dt/dx**2    
    print(F)
    u = np.zeros(Nx+1)
    u_1 = np.zeros(Nx+1)
    
    ue = np.zeros(Nx+1)         #used for true solution
    error = np.zeros(Nx+1)
    errmax = np.zeros(Nt+1)
    phi = np.zeros((Nx+1, Nt+1))
    
    for i in range(0, Nx+1):
        u_1[i] = U(x[i], 0)
    
    for n in range(1, Nt+1):
        for i in range(1, Nx):
            u[i] = u_1[i] + F*(u_1[i-1] - 2*u_1[i] + u_1[i+1])
            ue[i] = math.exp(-(math.pi)*(math.pi)*t[n])*math.sin(math.pi*(i)*dx)
            error[i] = ue[i]-u[i]

        u[0] = 0
        u[Nx] = 0
        
        u_1 = np.copy(u)
        errmax[n] = LA.norm(u, np.inf)
    
    Plots(x, u, ue, t, errmax, phi)
    
L = 1.0
a = 1.0
T = 0.1
Nx = 10
Nt = 20

FTCS(a, L, T, Nx, Nt)

    
    
    
    
    
    
