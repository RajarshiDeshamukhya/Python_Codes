#first order differential equation by scipy.integrate : dy/dx=x, y(0)=1
from scipy.integrate import odeint
#Define a function which calculates the derivative
import numpy as np
def dydx(y,x):
    return x
y0=1.0 #the initial condition: at x=0, y=1
x=np.linspace(0,2.0,3) #here we can change the step of linspace from 3 to 8 then check for a larger value of the function.
ys=odeint(dydx,y0,x)

print (ys)
