#first order diffential equation by scipy.integrate:dx/dt=3e^(-t), dy/dt=3-2y
#Initial condition : x(0)=0, y(0)=0
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
def f(u,t):
    x = u[0]
    y = u[1]
    dxdt = 3*np.exp(-t)
    dydt = 3-2*y
    return [dxdt,dydt]

u0 = [0,0]
t = np.linspace(0,10)
u = odeint(f,u0,t)
x = u[:,0]
y = u[:,1]
plt.xlabel("t")
plt.ylabel("x,y")
plt.plot(t,x,"r-")
plt.plot(t,y,"b-")
