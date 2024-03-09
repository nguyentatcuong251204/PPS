import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\NTCUONG\Downloads\data CK 20231 PPS\data CK 20231 PPS.csv",header=1)
print(df.head())
x=list(df.iloc[:,0])
y=list(df.iloc[:,1])
Z=[]
def gt(X,Y):
    for i in range(len(Y)):
        Z.append(Y[i]*X[i])
    return Z
Z=gt(x,y)
print(Z)
n=len(y)
h=0.125
def cong_thuc_hinh_thang(y,n,h):
    S=h*(y[0]+y[n-1])/2
    for i in range(1,len(y)-1):
        S+=h*y[i]
    return S
print(cong_thuc_hinh_thang(y,n,h))

def cong_thuc_Simpson(y,n,h):
    S=0
    for i in range(0,n-2,2):
        # print("y{}+4y{}+y{}".format(i,i+1,i+2),end=' ')
        S+=h/3*(y[i]+4*y[i+1]+y[i+2])
    return S
print(cong_thuc_Simpson(y,n,h))