#Runge Kutta 4
def f(x,y):
    return x+y**2

def rk4(xo,yo,xn,n):
    h=(xn-xo)/n
    for i in range(n):
        k1=h*(f(xo,yo))
        k2=h*(f(xo+h/2),(yo+k1/2))
        k3=h*(f(xo+h/2),(yo+k2/2))
        k4=h*(f(xo+h/2),(yo+k3))
        k=(k1+2*k2+2*k3+k4)/6
        yn=yo+k
        
        yo=yn
        xo=xo+h
    print(xn,yn)

xo=float(input("xo is:"))
yo=float(input("yo is:"))
xn=float(input("xn is:"))
step=int(input("Enter number of steps:")
         
rk4(xo,yo,xn,step)         
      
    