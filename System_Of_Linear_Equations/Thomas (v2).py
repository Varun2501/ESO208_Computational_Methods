import numpy as np

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
