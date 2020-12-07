import numpy as np

def F(x):
    return np.exp(float(x))

def Simpsons_1by3(a, b, N):
    
    h = (b-a)/N
    
    integral = 0
    
    for i in range(0, N-1, 2):
        
        x = a + h*i
        sum = (F(x) + 4*F(x+h) + F(x+2*h))*(h/3)
        integral = integral + sum
        
    return integral
    

def Simpsons_3by8(a, b, N):
    
    h = (b-a)/N
    
    integral = 0
    
    for i in range(0, N-2, 3):
        
        x = a + h*i
        sum = (F(x) + 3*F(x+h) + 3*F(x+2*h) + F(x+3*h))*(3*h/8)
        integral = integral + sum
        
    return integral

print(Simpsons_1by3(a, b, N))
print(Simpsons_3by8(a, b, N))

