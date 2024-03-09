import matplotlib.pyplot as plt
#Khoang nghiem [0,1] duoc chia lam 10 doan nen co 11 gia tri cua x
x=[]
y=[]
for i in range(11):
    x.append(i*0.2)
print(x)
y.append(0.5)
h=0.2
def f(x,y):
    return y-x**2+1

for i in range(1,11):
    y.append(y[i-1]+h*(f(x[i-1],y[i-1])+f(x[i],y[i-1]+h*f(x[i-1],y[i-1])))/2)

print(y)
