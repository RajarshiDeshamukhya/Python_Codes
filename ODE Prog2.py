#first order differential equation by scipy.integrate : dy/dx=x, y(0)=1. Find y at x=2
from scipy.integrate import odeint
#Define a function which calculates the derivative
import numpy as np
def dydx(y,x):
    return x
y0=1.0 #the initial condition: at x=0, y=1
x=[0,2]

ys=odeint(dydx,y0,x)
#output
print (ys)
print ('-----------------------')
print (ys[1:2])

