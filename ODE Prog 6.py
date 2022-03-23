#first order diffential equation by scipy.integrate:dy/dx=x-y, y(0)=1
from scipy.integrate import odeint 

# Define a function which calculates the derivatives

import numpy as np
import matplotlib.pyplot as plt
def dydx(y,x):
    return (x-y)

xs=np.linspace(0,5,100)
y0=1.0 #the initial condition
ys=odeint(dydx,y0,xs)
ys=np.array(ys).flatten()
plt.xlabel('x')
plt.ylabel('y')
#plt.plot(xs,ys,'r-')
y_exact=xs-1+2*np.exp(-xs)
y_diff= ys-y_exact
plt.plot(xs,ys,xs,y_exact,'b+')


