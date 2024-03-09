import matplotlib.pyplot as plt
#Khoang nghiem [0,1] duoc chia lam 10 doan nen co 11 gia tri cua x
x=[]
y=[]
for i in range(11):
    x.append(i*0.1)
print(x)
y.append(1)
h=0.1
def f(x,y):
    return y-2*x/y

for i in range(1,12):
    y.append(y[i-1]+h*f(x[i-1],y[i-1]))

print(y)



