import numpy as np
import math
import matplotlib.pyplot as plt
#Khởi tạo các giá trị x
def khoi_tao(left,right,h):
    x=[]
    n=int((right-left)/h)
    for i in range(n+1):
        x.append(left+i*h)
    return x
x=khoi_tao(3,4,0.2)
y=[]
z=[]
y.append(-2)
z.append(0)
def f(x,y,z):
    return math.exp(x)*z-2*y+1

for i in range(1,6):
    y.append(y[i-1]+0.2*z[i-1])
    z.append(z[i-1]+0.2*f(x[i-1],y[i-1],z[i-1]))

print(y)
print(z)

plt.plot(x,y)
plt.show()
