import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\NTCUONG\Downloads\Mực nước biển trung bình.txt",delimiter='\t')
X=[-0.463]
Y=[-133.8307292]
x=list(df['-0.463'])
y=list(df['-133.8307292'])
for value in x:
    X.append(value)
for value in y:
    Y.append(value)
value = float(input("NHAP X : "))
def chi_so_trai_khoang_cach_li(value):
    for i in range(len(x)):
        if (value-x[i])*(value-x[i+1]) < 0 :
            return i

X_noi_suy=[]
Y_noi_suy=[]
for i in range(2):
    X_noi_suy.append(x[chi_so_trai_khoang_cach_li(value)-2+i])
    Y_noi_suy.append(y[chi_so_trai_khoang_cach_li(value)-2+i])
for i in range(1,3):
    X_noi_suy.append(x[chi_so_trai_khoang_cach_li(value)+i])
    Y_noi_suy.append(y[chi_so_trai_khoang_cach_li(value)+i])

def yi_mul_Li(X,index,value):
    tu_so=1
    for i in range(len(X)):
        if i!=index:
            tu_so*=(value-X[i])
    mau_so=1
    for i in range(len(X)):
        if X[index]!=X[i]:
            mau_so*=(X[index]-X[i])
    return Y_noi_suy[index]*tu_so/mau_so
print(X_noi_suy)
print(Y_noi_suy)
def f_x(value):
    result=0
    for i in range(len(X_noi_suy)):
        result+=yi_mul_Li(X_noi_suy,i,value)
    return result

plt.scatter(X,Y)
plt.scatter(value,f_x(value),c='r')
plt.show()
        
