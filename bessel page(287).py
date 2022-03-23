#Bessel of 1st & 2nd kind
import numpy as np
import scipy.special as s
import matplotlib.pyplot as plt

x = np.linspace(0,20,300)

j0 = s.jn(0,x)
j1 = s.jn(1,x)
y0 = s.yn(0,x)
y1 = s.yn(1,x)

plt.plot(x,j0,'.-',label = 'j0',c='0.1')
plt.plot(x,j1,'--',label = 'j1',c='0.1')
plt.plot(x,y0,'-',label = 'y0',c='0.1')
plt.plot(x,y1,':',label = 'y1',c='0.1')

plt.title("Bessel Functions: 1st and 2nd kind", size ='10')
plt.legend(fontsize = 10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.ylim(-1,1)
plt.show()
