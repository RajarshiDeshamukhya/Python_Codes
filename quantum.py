import numpy as np
import matplotlib.pyplot as plt

m,h_bar,V,L = 1,1,10,10

x1 = np.sqrt((2*m*V)/(h_bar))
x0 = x1*L
x = np.linspace(0.1,10,1000)
y = np.sqrt(((x0**2)/(x**2)-1))
 
plt.xticks()
plt.yticks()
plt.plot(x,(np.tan(x)))
plt.plot(x,y)
plt.grid()
plt.show()
