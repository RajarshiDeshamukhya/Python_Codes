# double integration
from scipy.integrate import dblquad
from scipy.integrate import quad

f = lambda x,y:x+y
g = lambda x:2
h = lambda y:4
i=dblquad(f,0,1.0,g,h)
print(i)

import numpy as np
f = lambda x,y : np.sin(x+y)
g = lambda y:quad(f,0,np.pi,args=(y,))[0]
a=quad(g,-np.pi/2,np.pi/2)
print(a)