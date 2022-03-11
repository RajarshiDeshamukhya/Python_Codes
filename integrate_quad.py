from scipy import integrate
def f(x):
    return x**2
x=integrate.quad(f,2,5)
print(x)
 
    