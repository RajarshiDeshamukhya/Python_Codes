import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,20,10)
y=np.array([15.448      ,12.49466667 ,13.54133333 ,12.588      ,9.63466667 ,10.68133333
  ,9.728       ,8.77466667  ,7.82133333  ,6.868     ])

a=np.polyfit(x,y,1)
print(a)
'''
#for plotting graph
fig=plt.figure()
ax=fig.subplots()
ax.plot(x,a[0]*x+a[1],color="r")
ax.scatter(x,y)

plt.show()
'''




