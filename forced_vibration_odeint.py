import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def forced(u,t):
    x,v=u
    f=v
    g=F*np.cos(w*t)-lam*v-k*x
    return(f,g)

lam,k,F=0.5,5.0,1.0
t=np.arange(0,100,0.1)
u0=[0,1.0]
freq=np.arange(0.5,5,0.02)

A=[]
for w in freq:
    s=odeint(forced,u0,t)
    X=s[:,0]
    amp=np.max(X[-200:])
    A.append(amp)
     
exact=F/np.sqrt((k-freq**2)**2+lam**2*freq**2)

plt.plot(freq[::2],A[::2],'o',freq,exact,'-')
plt.show()     