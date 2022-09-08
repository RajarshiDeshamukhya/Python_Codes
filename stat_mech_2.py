import numpy as np
import matplotlib.pyplot as plt

mu = 70.0   #mu for mean, sigma for diff. standard deviation
sigma=2.0

x= mu + sigma*np.random.randn(10000)  #to change mean position
#print(x)
print("mean is:",np.mean(x))
print("standard deviation is:",np.std(x))
plt.hist(x)
plt.show()

#coin toss experiment
a=np.random.randint(0,2,100)  #randomly generating 0 or 1
print(a)
H=0
T=0
for i in range(100):
    if (a[i]==0):
        H=H+1
    else:
        T=T+1
print("No. of heads:",H)
print("No. of tail:",T)

#now if we want to run this program mulitple times and find out the average of all heads ans tails
H=[]  #this is using empty list
T=[]
for j in range(50):
    a=np.random.randint(0,2,100)
    h=0
    t=0
    
    for i in range(100):
        if (a[i]==0):
            h=h+1
        else:
            t=t+1
    H.append(h)
    T.append(t)
print("Heads:",H)
print("Tails:",T)    
    

#same program using array
H=np.zeros(500)  #we define empty arrays
T=np.zeros(500)
for j in range(500):
    a=np.random.randint(0,2,100)
    h=0
    t=0
    
    for i in range(100):
        if (a[i]==0):
            h=h+1
        else:
            t=t+1
    H[j]=h
    T[j]=t    
    
#print("Heads \n:",H)
#print("Average heads:",np.mean(H))
#print("Tails \n:",T)   
#print("Average tails:",np.mean(T)) 
plt.hist(H)    
plt.show()
        