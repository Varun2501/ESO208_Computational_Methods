import math; 

def f(x): 
  
       #return float(1 * pow(x, 3) + 2 * x * x + 10 * x - 20) 
       return None
  
def Muller(x1, x2, x3): 
  
    e = 1
    
    while (e>=0.0001): 
      

        f1 = f(x1); f2 = f(x2); f3 = f(x3); 

        f32 = (f3-f2)/(x3-x2)
        f21 = (f2-f1)/(x2-x1)
        f321 = (f32-f21)/(x3-x1)
        
        a = f321
        b = f32 + (x3-x2)*f321
        c = f3
        
        p = (b + abs(math.sqrt((b*b) - 4*a*c)))/(2*a)
        q = (b - abs(math.sqrt((b*b) - 4*a*c)))/(2*a)
        
        x_new_1 = x3 - p
        x_new_2 = x3 - q
        
        if abs(x_new_1-x3) > abs(x_new_2-x3):
            x_new = x_new_2
        else:
            x_new = x_new_1
            
        e = abs((x_new-x3)/x_new)
      
        x1, x2, x3 = x2, x3, x_new

    print(x_new)
    print(f(x_new))
  
a = 0 
b = 1 
c = 2
Muller(float(a), float(b), float(c)); 
