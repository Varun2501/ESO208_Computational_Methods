def g(x):
    return float() 
    
def FixedPoint(x): 
    
    e = 1
    n = 0
    
    while abs(e) >= 0.0001: 
        
        x_new = g(x)
        e = (x_new-x)/x
        x = x_new
        
        n = n+1 #no_of_iterations

    print("The value of the root is : ", "%.4f"% x) 
    
FixedPoint(x)
