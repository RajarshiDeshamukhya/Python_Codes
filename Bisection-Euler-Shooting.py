#Bisection Euler Shooting Method
import matplotlib.pyplot as plt
from math import log

def Euler(f,x,y0,yp0,dx):
    N=len(x)
    y=[0 for i in range(N)]
    y[0]=y0
    z=yp0
    for i in range(1,N):
        y[i]=y[i-1]+dx*z
        dz=f(x[i-1],y[i-1],z)
        z=z+dx*dz
    return y

def f(x,y,z): return -1.5*z #eqn. given

dx,x0,y0=0.001,0,1 #(set,given,given)
xN,yN=2/3*log(2),2 #(given,given)
yp01,yp02=-100,100 #(trial set, trial set)
tol=1e-5 #tolerance set

N=int((xN-x0)/dx) #calculating the iterations
dx=(xN-x0)/N #calculating the step size.
x=[x0+i*dx for i in range(N+1)] #calculating the value of x and storing in the array.
y=Euler(f,x,y0,yp01,dx) #the value of y using alpha1, setting the lower value of the function
dyN1=y[N]-yN
y=Euler(f,x,y0,yp02,dx) #the value of y using alpha2, setting the higher value of the function 
dyN2=y[N]-yN

if dyN1*dyN2<0:
    while True: #runs indefinitly
        yp0=0.5*(yp01+yp02)
        y=Euler(f,x,y0,yp0,dx)
        plt.plot(x,y)
        plt.plot(xN,yN,"X",c='k')
        plt.pause(1.0)
        plt.clf()
        dyN=y[N]-yN
        if dyN*dyN1<0:
            yp02=yp0
        else:
            yp01=yp0
        if(abs(dyN)<=tol):
            break
    print("Calculated value of dy/dx at x=0 is: ",yp0)
#    plt.plot(x,y)
#    plt.show()
else:
    print("Please choose another range of dy/dx at x=0")