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
    

print(Trapezoidal(1, 3, 3))
