import prutorlib as pl
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams
rcParams['figure.figsize'] = 5, 3

def p(x):
    return 1
    
def q(x):
    return (-(x+3)/(x+1))

def r(x):
    return ((x+3)/((x+1)**2))
    
def s(x):
    return 2*(x+1) + 3*r(x)

def Thomas_Algo(L, D, U, B): #Perform Thomas Algorithm
    
    n = len(L)
    P = np.zeros(n)
    Q = np.zeros(n)
    
    P[0] = D[0]
    Q[0] = B[0]
    
    for i in range(1, n):
        P[i] = D[i] - ((L[i]*U[i-1])/P[i-1])
        
    for i in range(1, n):
        Q[i] = B[i] - ((L[i]*Q[i-1])/P[i-1])
        
    X = np.zeros(n)
    X[n-1] = Q[n-1]/P[n-1]
    
    for i in range(n-2, -1, -1):
        X[i] = (Q[i] - (U[i]*X[i+1]))/P[i]
        
    return X
    
def Direct_Method(a, b, h, l, flag):
    
    n = int(l/h) 
    x = np.arange(n)*h
    print(x)
    
    L = np.zeros(n-1)
    D = np.zeros(n-1)
    U = np.zeros(n-1)
    B = np.zeros(n-1)
    
    for i in range(0, n-1):
        L[i] = p(x[i+1])/(h**2) - (q(x[i+1])/(2*h))
        
    for i in range(0, n-1):
        D[i] = -2*p(x[i+1])/(h**2) + r(x[i+1])
        
    for i in range(0, n-1):
        U[i] = p(x[i+1])/(h**2) + (q(x[i+1])/(2*h))
        
    for i in range(0, n-1):
        B[i] = s(x[i+1])

    
    B[0] = B[0] - L[0]*a
    #B[n-2] = B[n-2] - U[n-2]*b
    
    
    if flag == 1:
        print('Backward Difference')
        L[n-2] = L[n-2] - (U[n-2]/3)
        D[n-2] = D[n-2] + (4*U[n-2]/3)
        B[n-2] = B[n-2] - (2*U[n-2]*b*h/3)
    print(2*U[n-2]*b*h/3)
    L[0] = U[n-2] = 0
    
    X = Thomas_Algo(L, D, U, B)
    #print(L, D, U, B)
    
    print(X)
    
a = 5
b = 0
L = 2
h = 0.5
flag = 1

Direct_Method(a, b, h, L, flag)
