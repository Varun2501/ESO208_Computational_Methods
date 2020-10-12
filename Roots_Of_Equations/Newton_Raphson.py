def f(x):
    return float()
    
def df(x):
    return float() 
    
def NewtonRaphson(x): 
    
    e = 1
    
    while abs(e) >= 0.0001: 
        
        h = f(x) / df(x) 
        x_new = x - h 
        
        e = (x_new-x)/x_new
        x = x_new

    print("The value of the root is : ", "%.4f"% x) 
    
NewtonRaphson(x)
