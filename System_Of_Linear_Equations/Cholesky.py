import numpy as np

def Cholesky(a, b, n):

    L = np.zeros((n,n))
    
    for i in range(0, n):
        for j in range(0, i+1):
        
            s = sum(L[i][k] * L[j][k] for k in range(0,j))
            if (i == j): 
                L[i][j] = (a[i][i] - s)**(1/2)
            else:
                L[i][j] = ((a[i][j] - s)/L[j][j])

    print('Cholesky factor:\n', L, '\n')
    
    y = forward_substitution(np.concatenate((L, b), axis=1), n).reshape(n,1)
    x = backward_substitution(np.concatenate((L.T, y), axis=1), n)
    
    print('The Unknowns (X):', x, '\n') 
