import numpy as np
from numpy import random

def inputs():
    
    n = int(input())
   
    A = np.empty((n, n))
    for i in range(n):
        entries = list(map(float, input().split())) 
        A[i] = np.array(entries).reshape(1, n) 

    e = float(input()) 
    b = input()
    
    return n, A, e, b 

def Gram_Schmidt(n, A): #Return Q and R matrices
    
    Q = np.zeros((n, n))
    R = np.zeros((n, n))
    
    for i in range(n):
        v = A[:, i]
        s = 0
        
        for j in range(i):
            q = Q[:, j]
            R[j, i] = (v.T)@q
            s = s + (R[j, i]* q)
        z = v - s

        norm = 0
        for k in range(n):
            norm = norm + (z[k]*z[k])
        norm = (norm**0.5)
        
        Q[:, i] = z / norm
        R[i, i] = norm
        
    return Q, R

def QR_Decomposition(n, A, e):
    
    #Matrix having Determinant 0 is equivalent to Rank < n. Hence, I have used that condition due to minimise errors
    
    if np.linalg.matrix_rank(A) < n: 
        print('The Matrix is Singular: QR Decomposition cannot be performed')
        return None
    
    error = 1
    old_eigen = np.zeros(n)
    new_eigen = np.zeros(n)
    
    for i in range(n):
        old_eigen[i] = A[i][i]
    
    while(error>=e):
        Q, R = Gram_Schmidt(n, A)
        A = R@Q
        
        for k in range(n):
            new_eigen[k] = A[k][k]
        
        errors = np.subtract(new_eigen, old_eigen)
        error = np.max(errors)
        
        old_eigen = new_eigen
        new_eigen = np.zeros(n)
        
    print('The Eigen Values of the Matrix are:', np.round(old_eigen, 5))
 
def Inverse_Power_Method(n, A, e): 
    
    if np.linalg.matrix_rank(A) < n:
        print('The Absolute Minimum Eigen Value is 0')
        return None
    
    A_inv = np.linalg.inv(A)
    
    z = random.randint(10, size=(n, 1))
    z = A_inv@z

    error = 1
    eigen = 0
    
    while error >= e:
        
        max_eigen = abs(z[0])
        index = 0
        for i in range(1, n):
            if abs(z[i]) > max_eigen:
                index = i
		
        new_eigen = z[index]

        y = z/new_eigen
        error = abs((new_eigen - eigen)/new_eigen)
        eigen = new_eigen

        z = A_inv@y
    
    eigen = float(1/eigen)
    
    print('The Minimum Eigen Value is:', np.round(eigen, 6))
    
    eigen_vector = np.reshape(z/z[0], (1,n))
    print('The Corresponding Eigen Vector is: ', eigen_vector)
 
 
def Power_Method(n, A, e):
    
    z = random.randint(10, size=(n, 1)) #Generates Random Z
    z = A@z

    error = 1
    eigen = 0
    
    while error >= e:
        
        max_eigen = abs(z[0])
        index = 0
        for i in range(1, n):
            if abs(z[i]) > max_eigen:
                index = i
		
        new_eigen = z[index]

        y = z/new_eigen
        error = abs((new_eigen - eigen)/new_eigen)
        eigen = new_eigen

        z = A@y
    
    print('The Maximum Eigen Value is:', np.round(float(eigen), 6))
    
    eigen_vector = np.reshape(z/z[0], (1,n))
    print('The Corresponding Eigen Vector is: ', eigen_vector)
    
n, A, e, b = inputs()

if b == 'L':
    Power_Method(n, A, e)
    Inverse_Power_Method(n, A, e)
    
elif b == 'A':
    QR_Decomposition(n, A, e)
    
else:
    print('Wrong Input Format')
    
#Sample Input
'''
3
1 2 5 
3 5 7
4 8 0
0.00000000001
L

'''
#Size
#Matrix
#ErrorBound
#A/L 
