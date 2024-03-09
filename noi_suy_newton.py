import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("D:\document\data.xlsx") 
x=np.array(df.iloc[:,0])
y=np.array(df.iloc[:,1])

# print(df.head())
def bang_ti_sai_phan(y,x):
    X=np.zeros((len(y),len(y)),float)
    for i in range(len(y)):
        X[0][i]=y[i]
    for i in range(1,len(y)):
        for j in range(len(y)-i):
            X[i][j]=(X[i-1][j+1]-X[i-1][j])/(x[j+1]-x[j])
    return X

def f_x(value):
    result=y[0]
    tich_cac_hieu=1
    for i in range(len(y)-1):
        tich_cac_hieu*=(value-x[i])
        result+=tich_cac_hieu*bang_ti_sai_phan(y,x)[i+1][0]
    return result 

print(f_x(7))

