import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\NTCUONG\Downloads\data CK 20231 PPS\data CK 20231 PPS.csv",header=1) 

X=df.iloc[:,0]

Y=df.iloc[:,1]
Z=[]
def gt(X,Y):
    for i in range(len(Y)):
        Z.append(Y[i]*X[i])
    return Z
print(gt(X,Y))

n=len(Y)
def ti_sai_phan_c1(x,y):
    tsp=[]
    for i in range(n-1):
        tsp.append((Y[i+1]-Y[i])/(X[i+1]-X[i]))
    return tsp

def ma_tran_d(x,y):
    tsp=ti_sai_phan_c1(x,y)
    D=np.zeros((n,1),float)
    for i in range(1,n-1):
        D[i][0]=tsp[i]-tsp[i-1]
    return D

def ma_tran_A(x,y):
    A=np.zeros((n,n),float)
    A[0][0]=1
    A[n-1][n-1]=1
    for i in range(1,n-1):
        A[i][i-1]=(x[i]-x[i-1])/6
        A[i][i]=(x[i+1]-x[i])/3+(x[i]-x[i-1])/3
        A[i][i+1]=(x[i+1]-x[i])/6
    return A

def tinh_ma_tran_m(A,d):
    return np.linalg.inv(A)@d

A=ma_tran_A(X,Y)

d=ma_tran_d(X,Y)
m=tinh_ma_tran_m(A,d)

def khoang_nghiem(x):
    for i in range(n-1):
        if (X[i]-x)*(X[i+1]-x)<0:
            return i
        
