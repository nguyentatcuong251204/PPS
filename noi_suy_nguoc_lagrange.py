import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel(r"C:\Users\NTCUONG\data_science\data.xlsx")
x=np.array(df.iloc[:,0])
y=np.array(df.iloc[:,1])
# print(y.shape)
def bang_sai_phan(y):
    X=np.zeros((len(y),len(y)),float)
    for i in range(len(y)):
        X[0][i]=y[i]
    for i in range(1,len(y)):
        for j in range(len(y)-i):
            X[i][j]=(X[i-1][j+1]-X[i-1][j])
    return X

value=float(input("NHAP GIA TRI : "))

def don_dieu(y):
    l=[]
    def khoang_don_dieu(y):
        cac_cap_khoang_don_dieu=[]
        chi_so_ben_trai=0
        for i in range(len(y)-1):
            cap_khoang_don_dieu=[]
            if bang_sai_phan(y)[1][i] < 0 :
                cap_khoang_don_dieu.append(chi_so_ben_trai)
                cap_khoang_don_dieu.append(i)
                chi_so_ben_trai=i
                cac_cap_khoang_don_dieu.append(cap_khoang_don_dieu)
        return cac_cap_khoang_don_dieu
    for cap in khoang_don_dieu(y):
        if cap[1]-cap[0] == 1:
            continue
        else:
            l.append(cap)
    return l

# # print(chi_so_trai_khoang_cach_ly(value))
def kiem_tra_pp_ham_nguoc(value):
    check=False
    for cap in don_dieu(y):
        if (value-y[cap[0]])*(value-y[cap[1]]) < 0 :
            check=True
            return check,cap[0],cap[1]
    
def chi_so_trai_khoang_cach_ly(value):
    check,trai,phai=kiem_tra_pp_ham_nguoc(value)
    for i in range(trai,phai+1):
        if (value-y[i])*(value-y[i+1]) < 0:
            return i

def mang_y_va_mang_x(value):
    chi_so=[]
    for i in range(3):
        chi_so.append(chi_so_trai_khoang_cach_ly(value)+i-2)
    for i in range(2):
        chi_so.append(chi_so_trai_khoang_cach_ly(value)+i+1)
    
    mang_y=[]
    mang_x=[]
    for i in chi_so:
        mang_y.append(y[i])
        mang_x.append(x[i])
    return mang_y,mang_x

y_new,x_new=mang_y_va_mang_x(value)
def x_y(value,y,x):
    result=0
    def xi_mul_Li(value,y,x,index):
        tu_so=1
        for yi in y:
           tu_so*=(value-yi)
        tu_so/=(value-y[index])
        mau_so=1
        for yi in y:
            if y[index] != yi:
                mau_so*=(y[index]-yi)
        return x[index]*(tu_so/mau_so)
    for i in range(len(x)):
        result+=xi_mul_Li(value,y,x,i)
    return result

print(x_y(value,y_new,x_new))
        


