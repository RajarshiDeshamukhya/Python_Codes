import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as spo

def evenparity(x, x0):
    return np.tan(x) - np.sqrt((x0/x)**2 - 1)

def oddparity(x, x0):
    return 1.0/np.tan(x) + np.sqrt((x0/x)**2 - 1)

# Potential parameters
L = 6; V0 = 6; h_bar = 1; m = 1;

x0 =  L*np.sqrt(2*m*V0)/h_bar

# Plot even-parity transcendental equation to find the approximate solution
x = np.linspace(0.1, 20, 10000)
plt.figure(1)
plt.plot(x, np.tan(x), '--k+', lw=.4, label="tan(x)")
plt.plot(x, np.sqrt((x0/x)**2-1), '--g.', lw=.4, label = r"$\sqrt{(\frac{x_0}{x})^2-1}$")
plt.title("Finite Square Well (Even Parity)")
plt.legend(loc='best', prop={'size':18})
plt.xlabel("x", size=16)
plt.xticks(size = 14)
plt.ylabel(r"$f(x)$", size=16)
plt.yticks(size = 14)
plt.grid(b=True, which='both', color='0.65', linestyle='-')
plt.ylim([-20, 20])
plt.tight_layout()
plt.show()

# Plot odd-parity transcendental equation to find the approximate solution
plt.figure(2)
plt.plot(x, 1.0/np.tan(x), '--bx', lw=.4, label="cot(x)")
plt.plot(x, -np.sqrt(pow(x0/x,2)-1), '--r>', lw=.4, label = r"-$\sqrt{(\frac{x_0}{x})^2-1}$")
plt.title("Finite Square Well (Odd Parity)")
plt.legend(loc='best', prop={'size':18})
plt.xlabel("x", size=16)
plt.xticks(size = 14)
plt.ylabel(r"$f(x)$", size=16)
plt.yticks(size = 14)
plt.grid(b=True, which='both', color='0.65', linestyle='-')
plt.ylim([-20, 20])
plt.tight_layout()
plt.show()

# Appropriately guess the roots from graph
evenroot_guess = [1.5, 4.5, 7.0, 9.0]
oddroot_guess  = [2.0, 5.5, 9.5, 12.0]

# Compute x and check the authenticity of the roots
evenroot = spo.root(evenparity, evenroot_guess, args = (x0, ))
oddroot =  spo.root(oddparity,  oddroot_guess,  args = (x0, ))
print (evenroot.x)
print (oddroot.x)

# Compute energy
print ("Energy (even) = ", (evenroot.x*h_bar)**2/(2.0*m)-V0)
print ("Energy (odd)  = ", (oddroot.x *h_bar)**2/(2.0*m)-V0)
