import numpy as np

def F(x):
    return np.exp(float(x))

def Trapezoidal(a, b, N):
    
    h = (b-a)/N
    
    integral = 0
    
    for i in range(N):
        
        x = a + h*i
        sum = (F(x) + F(x+h))*(h/2)
        integral = integral + sum
        
    return integral
    

def Romberg(a, b, N, n):
    
    I = np.zeros(n)
    
    for i in range(n):
        N_new = N*(2**i) #increase sub-intervals by a factor of 2
        I[i] = Trapezoidal(a, b, N_new)
           
    for i in range(1, n):
        for j in range(n-1):
            
            I[j] = ((4**i)*I[j+1] - I[j])/((4**i)-1)
    
    integral = I[0]
    
    print(integral)


print(Trapezoidal(1, 10, 6))
Romberg(1, 10, 6, 3)
