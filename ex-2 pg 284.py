# To find the following relation in page 284, Exercise:2

import numpy as np
import math as mt
from scipy.special import legendre

n=int (input ("Enter the number :"))
theta=float (input ("Enter the angle :"))

thetad = ((mt.pi)/180)*theta*(n+1)
thetadd= ((mt.pi)/180)*theta
y=(mt.sin(thetad))/(mt.sin(thetadd))
print ("\nL.H.S of the identity =",(format(y,'.3f')))

a=mt.cos(thetadd)
sum=0
for i in range (0,n+1):
   p0=legendre(i)(a)*legendre(n-i)(a)
   sum=sum+p0
   
print ("R.H.S of the identity =",(format(sum,'.3f')))

