#Registration No: 
#Roll No:
#Problem8: TISE forradial part of anharmonic oscillator
#Date:

import numpy as np
import scipy
from scipy.integrate import odeint
from scipy.optimize import newton
import matplotlib.pyplot as plt

# Return TISE 
def schroed(y, r, l, E):
    psi, phi = y
    k = 1.0; b = 2.0;
    dVdr = [phi, ((l*(l+1))/(r**2) + k*r**2 + 2.0*b*r**3/3 - 2.0*E)*psi]
    return np.asarray(dVdr)

# Shooting: Solve dphi/dx = f(psi,x,V,E) with psi(x[0]) = psi0 for energy array.
def shoot_odeint(func, psi_init, x, l, E):
    psi_rightb = []
    for EN in E:
        psi = odeint(schroed, psi_init, x, args=(l,EN))[:,0]
        psi_rightb.append(psi[len(psi)-1])
    return np.asarray(psi_rightb)

# Helper function for optimizing results using odeint
def shoot_optim(E, psi_init, x, l):
    sol = odeint(schroed, psi_init, x, args=(l,E))
    return sol[len(sol)-1][0]

# Find zero crossing due to sign change in rightbound array. Return array with
# indices before sign changes
def findZeros(rightb):
    return np.where(np.diff(np.signbit(rightb)))[0]

# Optimize energy for function using Newton-Raphson method
def optimizeEnergy(func, psi0, x, l, E):
    shoot = shoot_odeint(func, psi0, x, l, E)
    crossings = findZeros(shoot)
    energy = []
    for cross in crossings:
        energy.append(newton(shoot_optim, E[cross], args=(psi_init, x, l)))
    return np.asarray(energy)

# Normalize wave function
def normalize(output_wavefunc):
    normal = max(output_wavefunc)
    return output_wavefunc*(1/normal)

# Shooting: returns numeric solution only
def rao_shoot(psi_init, h, l, xl, xr, El, Eh, dE):
    x = np.arange(xl, xr, h)
    E = np.arange(El, Eh, dE)
    eigEnl = optimizeEnergy(schroed, psi_init, x, l, E)
    psi_num = []
    for EN in eigEnl:
        out = odeint(schroed, psi_init, x, args=(l,EN)) 
        psi_num.append(normalize(out[:,0]))
    print ("Eigenstate energy ", eigEnl)   
    return x, np.asarray(psi_num)

# Output Wave-functions
def plot_wavefun(fig, title_string, x, psi_num):
    plt.cla() 
    plt.clf() 
    plt.plot(x, psi_num,            'ko', linewidth=1, label=r"$\Psi(\hat{x})_{num}$")
    plt.ylabel(r"$\Psi(\hat{x})$", fontsize=16)
    plt.xlabel(r'$\hat{x}$',       fontsize=16)
    plt.legend(loc='best', fontsize='small')
    plt.axis([x.min()-0.2, x.max()+0.2, -2.2, 1.2])
    plt.title(title_string)
    plt.grid()
#    fig.savefig("plot/wavefunc_"+title_string+".png")

# MAIN
# Initial conditions 
psi_0 = 0.0; phi_0 = 1.0
psi_init = np.asarray([psi_0, phi_0])
h = 1.0/200                         # stepsize 
xl = -2.0; xr = 2.0+h;              # Abscissa bracket
El = 0.0;   Eh = 20.0; dE = 0.001;  # Energy bracket

# Peform Integration
x, psi_num = rao_shoot(psi_init, h, 0, xl, xr, El, Eh, dE) # 1s, 2s, 3s

# Plot wavefunction
fig = plt.figure()
plot_wavefun(fig, "RAO_1s", x,   psi_num[0,:])
plt.show()
plot_wavefun(fig, "RAO_2s", x,   psi_num[1,:])
plt.show()
plot_wavefun(fig, "RAO_3s", x,   psi_num[2,:])
plt.show()
