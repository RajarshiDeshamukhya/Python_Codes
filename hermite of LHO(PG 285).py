#LHO using hermite polynomial
import numpy as np
import math as mt
from scipy.special import hermite
import matplotlib.pyplot as plt

x=np.linspace (-3,3,100)

def psi(n,x):
    Hn=hermite (n)
    return (1/np.sqrt(2**n*mt.factorial(n))*pow(1/np.pi,0.25)*np.exp(-x**2/2)*Hn(x))

for n in range (3):
    plt.subplot(1,3,n+1)
    plt.tight_layout(pad=0.75)
    plt.plot(x,psi(n,x),lw=2)
    plt.xlim(-3,3)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.title("n=%d" %n, size=20)
    
plt.show()    
