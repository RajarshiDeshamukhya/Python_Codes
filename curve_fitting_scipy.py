from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

def f(x,a,b):
    return a*x+b

x=np.linspace(0,20,10)
y=np.array([15.448      ,12.49466667 ,13.54133333 ,12.588      ,9.63466667 ,10.68133333
  ,9.728       ,8.77466667  ,7.82133333  ,6.868     ])

param,param_cov=optimize.curve_fit(f,x,y)

print(param[0],param[1])