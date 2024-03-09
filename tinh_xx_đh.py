import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv(r"C:\Users\NTCUONG\Downloads\Mực nước biển trung bình.txt",delimiter='\t')
X=list(df['-0.463'])
X=[-0.463]+X
Y=list(df['-133.8307292'])
Y=[-133.8307292]+Y
value=0.628


# print(df.head)
def bang_sai_phan(Y):
    Z=np.zeros((len(Y),len(Y)),float)
    for i in range(len(Y)):
        Z[0][i]=Y[i]
    for i in (1,len(Y)):
        for j in range(len(Y)-i):
            Z[i][j]=Z[i-1][j+1]-Z[i-1][j]
    return Z

def tinh_xx_dh(h):
    result=0
    Z=bang_sai_phan(Y)
    for i in range(1,len(Y)):
        result+=1/h*pow(-1,i+1)*Z[i][0]
    return result



