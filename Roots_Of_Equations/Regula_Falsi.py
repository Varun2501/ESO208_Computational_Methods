def f(x):
    return float(x*x - 5*x + 6)
   
def RegulaFalsi(xl, xu): 
    
    e = 1
    
    while e >= 0.0001: 
        
        h = (f(xu)-f(xl))/(xu-xl)
        x = xl - f(xl)/h

        
        if f(xl)*f(x) < 0: 
            xu = x
        else:
            xl = x
            
        e = (xu - xl)/2.0 

    print("The value of the root is : ", "%.5f"% x) 
    
RegulaFalsi(2.5, 3.7)
