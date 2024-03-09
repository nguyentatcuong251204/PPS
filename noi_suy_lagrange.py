import pandas as pd
import numpy as np

df=pd.read_csv(r"C:\Users\NTCUONG\Downloads\Mực nước biển trung bình.txt",delimiter='\t')
X=[-0.463]
x=list(df['-0.463'])
for value in x:
    X.append(value)
Y=[-133.8307292]
y=list(df["-133.8307292"])
for value in y:
    Y.append(value)

value=float(input("NHAP x : "))
def yi_mul_Li(value,X,index):
    tu_so=1
    for i in range(len(X)):
        if (index != i):
            tu_so*=(value-X[i])
        else:
            continue
    
    mau_so=1
    for i in range(len(X)):
        if (X[index] != X[i]):
            mau_so*=(X[index]-X[i])
        else:
            continue
    return Y[index]*tu_so/mau_so
    # return mau_so

def noi_suy_lagrange(value):
    result=0
    for i in range(len(X)):
        result+=yi_mul_Li(value,X,i)
    return result

print(noi_suy_lagrange(value))



