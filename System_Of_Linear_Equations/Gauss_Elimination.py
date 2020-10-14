import numpy as np

def inputs():
    n = int(input())
   
    entries = list(map(float, input().split())) 
    a = np.array(entries).reshape(n, n) 

    entries = list(map(float, input().split())) 
    b = np.array(entries).reshape(n, 1) 
    
    c = input()
    
    return n, a, b, c 

def gauss_elimination(a, b, n):
      
    P = np.identity(n)
    R = np.identity(n)
    l = np.ones((3,3))
    flags = []
    
    for i in range(n):
        a, b, P = pivot(a, b, n, P, i)
        
        '''if abs(max(a[:,i])) <0.001:                     #if_scaling_is_done
            R[i][i] = 1000 #scaling by a factor of 1000
            a = a@R
            R = np.identity(n) #reset the scaling factor
            flags.append(i)'''

        for j in range(i+1, n):
            l[j][i] = a[j][i]/a[i][i]
            for k in range(0,n):
                a[j][k] = a[j][k] - (a[i][k]*l[j][i]) 
            b[j] = b[j] - b[i]*l[j][i]  

    if a[n-1][n-1] == 0: raise ValueError('No Unique Solution')
    
    m = np.concatenate((a,b), axis=1)
    x = backward_substitution(m, n)
    
    '''for i, flag in enumerate(flags):  #if_scaling_is_done
        x[flag] = x[flag]*1000'''
    
    np.set_printoptions(suppress=True)
    print('The Unknowns (X):', x, '\n')
    print('Permutation Matrix1 (pre-multiply):\n', P, '\n')
    print('Elements of U:\n', m)
    
    return None

def backward_substitution(m, n):
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        s = sum(m[i][j] * x[j] for j in range(i, n))
        x[i] = (m[i][n] - s) / m[i][i]
    return x

def forward_substitution(m, n):
    x = np.zeros(n)
    for i in range (0, n):
        s = sum(m[i][j] * x[j] for j in range(0, i))
        x[i] = (m[i][n]-s)/m[i][i]
    return x

def pivot(a, b, N, P, i):

    max_ = abs(a[i][i])
    m = i

    for j in range(i, n):
        if(abs(a[j][i])>max_):
                m=j
    
    p = np.identity(N)
    p[m][m] = p[i][i] = 0
    p[m][i] = p[i][m] = 1 
     
    a = p@a
    b = p@b
    P = p@P
    
    return a, b, P
    
n = 3
a = np.asarray([4, 2, 0, 2, 4, 1, 0, 1, 5]).reshape(n, n)
b = np.asarray([10, 11.5, 5]).reshape(n, 1)
gauss_elimination(a, b, n)
