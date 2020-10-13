import numpy as np
import cmath

def Bairstow(n, a, r, s, x):

    if n < 1:
        return None
    
    elif (n==1 and a[1]!=0):
        x.append(float(-a[0])/float(a[1]))
        return None

    elif (n==2):
        x1 = (-a[1] + cmath.sqrt((a[1]*a[1]) - 4*a[2]*a[0]))/(2.0*a[2])
        x2 = (-a[1] - cmath.sqrt((a[1]*a[1]) - 4*a[2]*a[0]))/(2.0*a[2])
        x.append(x1)
        x.append(x2)
        return None

    if n>2:
 
        e_r = float(1)
        e_s = float(1)
        while e_r>=1E-14 and e_s>=1E-14:
           
            b = np.zeros(n+1)
            c = np.zeros(n+1)
            b[n] = a[n]
            b[n-1] = a[n-1] + r*b[n]
            for i in range(n-2, -1, -1):
                b[i] = a[i] + r*b[i+1] + s*b[i+2]
                
            c[n] = b[n]
            c[n-1] = b[n-1] + r*c[n]
            for i in range(n-2, -1, -1):
                c[i] = b[i] + r*c[i+1] + s*c[i+2]
            
            c_m = np.asarray([c[1], c[2], c[2], c[3]]).reshape(2,2)
            c_m_inv = np.linalg.inv(c_m)
            b_m = np.asarray([-b[0], -b[1]]).reshape(2,1)
            d = c_m_inv@b_m

            r_new = r+d[0]
            s_new = s+d[1]

            e_r = abs((r_new-r)/r)
            e_s = abs((s_new-s)/s)

            r = r_new
            s = s_new

        if (r*r) + 4*s == 0:
            x.append(r/2)
        else:
            x1 = (r + cmath.sqrt((r*r) + 4*s))/2
            x2 = (r - cmath.sqrt((r*r) + 4*s))/2
            x.append(x1)
            x.append(x2)
                
        return Bairstow(n-2, b[2:], r, s, x)

x = []        
#a = [-24, -26, 3, 6, 1] a0, a1, ....
#n = 4
#Bairstow(order, poly, r, s, solution)
Bairstow(n, a, 3, 2, x)
print(x)
    
