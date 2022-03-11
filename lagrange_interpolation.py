#Lagrange Interpolation

import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

#using maths finding interpolated point
n=int(input("Enter no. of data points:"))
x=np.zeros((n))
y=np.zeros((n))
for i in range(n):
    x[i]=float(input( 'x['+str(i)+']='))
    y[i]=float(input( 'y['+str(i)+']='))
xp=0.35
yp=0
for i in range(3):
    p=1
    for j in range(3):
        if i!=j:
            p=p*(xp-x[j])/(x[i]-x[j])
    yp=yp+y[i]*p
print("The interpolated point is:",yp)

#using np
x=np.array(x) 
y=np.array(y) 
yp=lagrange(x,y)  
print("The interpolated point is:",yp)

#to plot the graph
a=np.polynomial.polynomial.Polynomial(yp).coef

x_new=np.arange(0.2,0.7,0.1)
#print(x_new)
#plt.figure(figsize=(10,8))
plt.plot(x_new,yp(x_new),'b',x,y,'ro' )
plt.grid()
plt.show()            
                  
print(yp([0.35])) 