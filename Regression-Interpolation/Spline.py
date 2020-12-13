import prutorlib as pl
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams
rcParams['figure.figsize'] = 5, 3

def inputs():
    
    entries = list(map(float, input().split())) 
    x = np.asarray(entries) 

    entries = list(map(float, input().split())) 
    y = np.asarray(entries)
    
    a = float(input())
    b = input()
    
    return x, y, a, b

def table(x, y): #Calculate h and g
    
    n = len(x)
    h = np.zeros(n-1)
    g = np.zeros(n-1)
    
    for i in range(n-1):
        
        h[i] = float(x[i+1] - x[i])
        g[i] = float((y[i+1] - y[i])/h[i])
        
    return h, g

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

def Cubic_Spline_Matrix(V, x, y, g, h, i): #Return Coefficients of Cubic Spline Matrix
    
    A = V[i+1]/(6*h[i])
    B = V[i]/(6*h[i])
    C = (y[i+1]/h[i]) - ((V[i+1]*h[i])/6)
    D = (y[i]/h[i]) - ((V[i]*h[i])/6)
    
    return np.asarray([A, B, C, D])

def Cubic_Spline_Value(Q, x, i, a): #Calculate value at the required point
    
    A = Q[i][0] 
    B = Q[i][1]
    C = Q[i][2]
    D = Q[i][3]
    
    
    Value = (A*((a-x[i])**3)) - (B*((a-x[i+1])**3)) + (C*(a-x[i])) - (D*(a-x[i+1]))
    return Value
    
def Plot(Q, x, y, a, Value): #Plot the Spline
    
    n = len(x)
    
    for i in range(n-1):
        X = np.linspace(x[i], x[i+1], 100)
        Y = Cubic_Spline_Value(Q, x, i, X)
        plt.plot(X, Y)
        plt.tight_layout()
    
    plt.scatter(x, y, s=10, color='k', zorder=10)
    
    if Value:
        plt.scatter(a, Value, s=10, color='blue', zorder=10) #Plot the point in blue if its inside data range
         
    pl.prutorsaveplot(plt, 'plot2d.pdf')
    
    
def Natural_Spline(x, y, a):
    
    print('Natural Spline\n')
    
    h, g = table(x, y)
    
    n = len(x)
    L = np.zeros(n-2)
    D = np.zeros(n-2)
    U = np.zeros(n-2)
    B = np.zeros(n-2)
    
    for i in range(1, n-2):
        L[i] = h[i]
        
    for i in range(n-2):
        D[i] = 2*(h[i]+h[i+1])
        
    for i in range(0, n-3):
        U[i] = h[i+1]
        
    for i in range(n-2):
        B[i] = 6*(g[i+1] - g[i])


    X = Thomas_Algo(L, D, U, B)
    V = np.zeros(n)
    for i in range(1, n-1):
        V[i] = X[i-1]
    
    Q = np.empty((n-1,4))
    for i in range(n-1):
        Q[i] = Cubic_Spline_Matrix(V, x, y, g, h, i)

    print('The Coefficent Matrix Ai Bi Ci Di is: ')
    print(np.round(Q, 5), '\n')
        
    min_i = 0
    for i in range(n):
        if (a > x[i]): 
            min_i = i
            
    if min_i < (n-1):        
        Value = Cubic_Spline_Value(Q, x, min_i, a)
        print('The Interpolated Function Value is: ', Value)
        Plot(Q, x, y, a, Value)
    
    elif min_i == (n-1):
        print('The Interpolating Value is Out of Range')
        Plot(Q, x, y, a, Value=None)
    
    return None
 
def Not_A_Knot_Spline(x, y, a):
    
    print('Not-A-Knot Spline\n')
    
    h, g = table(x, y)
    n = len(x)
    
    Z = np.zeros((n, n))
    B = np.zeros((n, 1))
    
    j = 0
    for i in range(1, n-1):
        Z[i][j] = h[i-1]
        Z[i][j+1] = 2*(h[i] + h[i-1])
        Z[i][j+2] = h[i]
        j = j + 1
     
    Z[0][0] = h[1]
    Z[0][1] = -(h[0] + h[1])
    Z[0][2] = h[0]
    
    Z[n-1][n-3] = h[n-2]
    Z[n-1][n-2] = -(h[n-2] + h[n-3])
    Z[n-1][n-1] = h[n-3]
        
    for i in range(1, n-1):
        B[i] = 6*(g[i] - g[i-1])  
    
    S = (np.linalg.inv(Z))@B
    V = np.zeros(n)
    for i in range(n):
        V[i] = S[i][0]
        
    
    Q = np.empty((n-1,4))
    for i in range(n-1):
        Q[i] = Cubic_Spline_Matrix(V, x, y, g, h, i)

    print('The Coefficent Matrix Ai Bi Ci Di is: ')
    print(np.round(Q, 5), '\n')
        
    min_i = 0
    for i in range(n):
        if (a > x[i]): 
            min_i = i
            
    if min_i < (n-1):        
        Value = Cubic_Spline_Value(Q, x, min_i, a)
        print('The Interpolated Function Value is: ', Value)
        Plot(Q, x, y, a, Value)
    
    elif min_i == (n-1):
        print('The Interpolating Value is Out of Range')
        Plot(Q, x, y, a, Value=None)
    
    return None
    
x, y, a, b = inputs()   

if b == 'A':
    Natural_Spline(x, y, a) 
    
elif b == 'B':
    Not_A_Knot_Spline(x, y, a)


#Sample Input   
''' 
0.000 0.500 1.000 1.500 2.000
1.000 1.649 2.718 4.482 7.389
1.75
A
 '''
# Input Format 
# Xi
# Yi
# X value for which interpreted function value has to be calculated
# A/B: A for Natural Spline and B for Not-a-knot

