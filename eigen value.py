#eigen value of the LHO

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as spo




def evenparity(x, x0):
    return (np.tan(x) - np.sqrt((x0/x)**2 - 1 ))

def oddparity(x, x0):
    return (1.0/np.tan(x) + np.sqrt((x0/x)**2 -1 ))

m=1
v=6
h_bar=1
L=6

x0=L*np.sqrt((2*m*v)/(h_bar))

x=np.linspace(0.1,20,10000)
y=np.sqrt(((x0**2)/(x**2)-1))


plt.figure(1)

plt.xlim(0,10)
plt.ylim(-20,20)
plt.plot(x,(np.tan(x)))
plt.plot(x,y)
plt.grid()
plt.title('plot of tan(x)')
plt.show()


plt.figure(2)

plt.xlim(0,10)
plt.ylim(-20,20)
plt.plot(x,(1/(np.tan(x))))
plt.plot(x,-y)
plt.grid()
plt.title('plot of cot(x)')
plt.show()

evenroot_guess=[1.5, 4.5, 7.0, 9.0]
oddroot_guess=[2.0, 5.5, 9.5, 12.0]

evenroot = spo.root(evenparity, evenroot_guess, args = (x0, ))
oddroot =  spo.root(oddparity,  oddroot_guess,  args = (x0, ))
print (evenroot.x)
print (oddroot.x)

#Compute energy
print ("Energy (even) = ", (evenroot.x*h_bar)**2/(2.0*m*L**2))
print ("Energy (odd)  = ", (oddroot.x *h_bar)**2/(2.0*m*L**2))

