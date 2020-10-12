def f(x):
    return float()
    
def Bisection(xl, xu): 
    
    e = 1
    
    while e >= 0.001: 
        
        x = (xu + xl)/2.0
        
        if f(xl)*f(x) < 0: 
            xu = x
        else:
            xl = x
            
        e = (xu - xl)/2.0 


    print("The value of the root is : ", "%.3f"% x) 
    
Bisection(xl, xu)
