import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_excel("D:\document\data.xlsx")
x=np.array(df.iloc[:,0])
y=np.array(df.iloc[:,1])
h=0.1

def t(value):
    return (value-x[0])/h

def giaithua(n):
    if n==0:
        return 1
    else:
        return n*giaithua(n-1)
    
def bang_sai_phan(y):
    X=np.zeros((len(y),len(y)),float)
    for i in range(len(y)):
        X[0][i]=y[i]
    for i in range(1,len(y)):
        for j in range(len(y)-i):
            X[i][j]=X[i-1][j+1]-X[i-1][j]
    return X

# print(bang_sai_phan(y))

def f_x(value):
    result=y[0]
    t_mul=1
    for i in range(1,len(y)):
        t_mul*=(t(value)-i+1)
        result+=bang_sai_phan(y)[i][0]*t_mul/giaithua(i)
    return result
plt.scatter(x,y)
plt.show()