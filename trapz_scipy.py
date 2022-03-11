import numpy as np
from scipy import integrate

def f(x):
    return (x+1/x)

x=np.linspace(1.2,1.6,5)
v=np.vectorize(f)
y=v(x)
a=integrate.trapz(y,x)
print(a)
