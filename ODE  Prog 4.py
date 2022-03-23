#first order differential equation by scipy.integrate : dy/dx=x, y(0)=1. 

#first order differential equation by scipy.integrate : dy/dx=x, y(0)=1. Find y at x=2
from scipy.integrate import odeint
#Define a function which calculates the derivative
import numpy as np
import matplotlib.pyplot as plt
def dydx(y,x):
    return x


xs=np.linspace(0,5,100) #here we can change the step of linspace from 3 to 8 then check for a larger value of the function.
y0=1.0 # the initial condition: at x=0 , y=1 
ys=odeint(dydx,y0,xs)
ys=np.array(ys).flatten()# convert to a single array

plt.xlabel('x')
plt.ylabel('y')
#plt.plot(xs,ys)
y_exact=xs*xs/2+1
y_diff= ys - y_exact
plt.plot(xs,ys,'r')
plt.plot(xs,y_exact,'b')
plt.grid()
plt.show()
print (y_diff)
 

