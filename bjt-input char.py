import matplotlib.pyplot as plt

Vbe1 =[0.3,0.33,0.36,0.37,0.39,0.40,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.48,0.49,0.49,0.5,0.5,0.51,0.52,0.52,0.52,0.53,0.53,0.54,0.55]
Ib1 =[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2,1.3,1.7,1.8,1.9,2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1]

Vbe2 =[0.23,0.28,0.34,0.36,0.37,0.38,0.39,0.40,0.40,0.41,0.42,0.42,0.44,0.45,0.46,0.47,0.74,0.48,0.49,0.49,0.50,0.51,0.51,0.52,0.53]
Ib2 =[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.10,1.1,1.2,1.3,1.4,1.6,1.7,1.8,2.0,2.1,2.3,2.4,2.6,2.7,2.9,3.0]

plt.plot(Vbe1,Ib1,'-o')
plt.plot(Vbe2,Ib2,'-o')
plt.show()
     
