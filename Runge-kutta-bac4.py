import matplotlib.pyplot as plt
import numpy as np
#Khoang nghiem [0,1] duoc chia lam 10 doan nen co 11 gia tri cua x
x=[]
y=[]
z=[]
y.append(0.8)
z.append(0.3)
h=0.01
for i in range(1001):
    x.append(i*0.1)

def f(x,y):
    return x*(1-x)*(x-0.14)-0.2*x*y
def g(x,y):
    return 0.6*x*y-0.45*y
def cal(y):
    for i in range(1,1001):
        k=[]
        value=y[i-1]
        k.append(h*f(x[i-1],y[i-1]))
        value+=1/6*k[0]
        k.append(h*f(x[i-1]+h/2,y[i-1]+k[0]/2))
        value+=1/3*k[1]
        k.append(h*f(x[i-1]+h/2,y[i-1]+k[1]/2))
        value+=1/3*k[2]
        k.append(h*f(x[i-1]+h,y[i-1]+k[2]))
        value+=1/6*k[3]
        y.append(value)
    return y
def cal1(y):
    for i in range(1,1001):
        k=[]
        value=y[i-1]
        k.append(h*g(x[i-1],y[i-1]))
        value+=1/6*k[0]
        k.append(h*g(x[i-1]+h/2,y[i-1]+k[0]/2))
        value+=1/3*k[1]
        k.append(h*g(x[i-1]+h/2,y[i-1]+k[1]/2))
        value+=1/3*k[2]
        k.append(h*g(x[i-1]+h,y[i-1]+k[2]))
        value+=1/6*k[3]
        y.append(value)
    return y

m=cal(y)
n=cal1(z)
plt.plot(m,n)
plt.show()

