#import random numbers
import numpy as np
import matplotlib.pyplot as plt
x=np.random.randint(0,101)
print(x)  #for single number

x=np.random.randint(0,101,20)
print(x)  #specify no. of random numbers

#plotting histogram
x=np.random.randint(0,101,1000)
plt.hist(x,bins=[0,10,20,30,100])  #2nd argument is for no. of divisions
plt.show()  #uniform distribution 

x=np.random.rand(10)   #default limit is o-1 and 10 is no. of numbers 
print(x) 

#normal distribution
x=np.random.randn(1000) #generates 1000 normally distributed numbers around x=0
print(x)
plt.hist(x,10)
plt.plot() 

