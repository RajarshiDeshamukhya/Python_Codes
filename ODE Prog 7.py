#second order differential equation: d^2x/dt^2+ a(dx/dt) + cx=0
#Initial condition : x(0)=0, y(0)=1, a=0.5, b=1.2, c=0
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
def f(u,t):
    x,y=u
    z=y
    g=c-b*x-a*y
    return [z,g]
a,b=0.5,2.5
c=0
u0=[0,1]
t=np.linspace(0,20,100)
#Solution
r=odeint(f,u0,t)
x=r[:,0]#1st column
y=r[:,1]#2nd column

#Plotting
plt.xlabel('x')
plt.ylabel('y')
plt.title('OSCILLATORY')
plt.plot(t,x,'r-')
plt.plot(t,y,'b-')
plt.grid()
plt.show()
