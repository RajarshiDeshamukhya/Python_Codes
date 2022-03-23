import numpy as np
import matplotlib.pyplot as plt

names=[]
marks=[]

f=open('sample.txt','r')
while True:
    data=f.readline().split()
    if not data:
        break
    
    names.append(data[0])
    marks.append(int(data[1]))
f.close()
    


plt.plot(names,marks, '-o',c='r', label='the data')
plt.grid()



plt.show()
