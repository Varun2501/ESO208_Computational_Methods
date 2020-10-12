def f(x):
    return float()
      
def Secant(x1, x2): 
    
    e = 1
    
    while abs(e) >= 0.0001: 
        
        df = (f(x1)-f(x2))/(x1-x2)
        x_new = x2 - f(x2)/df
        
        e = (x_new-x2)/x_new
        x1, x2 = x2, x_new

    print("The value of the root is : ", "%.4f"% x_new) 
    
Secant(x1, x2)
