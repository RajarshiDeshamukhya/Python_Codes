#Hermite graph plotting
import numpy as np
from scipy.special import hermite
import matplotlib.pyplot as plt
from itertools import cycle

x = np.linspace(-10,10,150)
lines = ['-','--','-.',':','..']
linecycler = cycle(lines)

for i in range(2,6):
    plt.plot(x,hermite(i)(x),lw=2,ls=next(linecycler))
    
plt.xlim(-3 ,3)    
plt.ylim(-7,7)    
plt.legend(['$H_2$','$H_3$','$H_4$','$H_5$'],fontsize=10)
plt.title("Hermite Polynomial")
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid()
plt.show()
