# To write a code for the Legendre Polynomial for the followig recurrance relation
# nP_n(x)=(2n-1)xP_(n-1)(x)-(n-1)P_(n-2)(x)


import numpy as np
from scipy.special import legendre

n=int (input ("Enter the number (n):"))
x=int (input ("Enter the number (x):"))

p=legendre(n)
a=n*p(x)
print ('nP_n(x) =',a)

p1=legendre(n-1)
p2=legendre(n-2)
b=(2*n-1)*x*p1(x)
c=(n-1)*p2(x)
x=b-c
print ('(2n-1)xP_(n-1)(x)-(n-1)P_(n-2)(x) =',x,'\n')

if a==x:
    print ('The following Legendre Recurrance relation matches.')

