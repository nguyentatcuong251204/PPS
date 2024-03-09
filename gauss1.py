import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("D:\document\data.xlsx") 
x=np.array(df.iloc[:,0])
y=np.array(df.iloc[:,1])
x=list(x)
y=list(y)
# value=float(input("nhap gia tri : "))
def bang_sai_phan_c1(y):
    bang=[]
    for i in range(len(y)-1):
        bang.append(y[i+1]-y[i])
    return bang

def mang_cac_chi_so_ben_trai_kcl(value):
    mang=[]
    for i in range(len(x)-1):
        if (value-x[i])*(value-x[i+1]) < 0:
            mang.append(i)
    return mang

def mang_cap_chi_so_khoang_don_dieu(y):
    def mang_tam(y):
        mang_cac_cap_chi_so=[]
        chi_so_ben_trai=0
        for i in range(len(bang_sai_phan_c1(y))-1):
            mang_cap_cs=[]
            
            if (bang_sai_phan_c1(y)[i] < 0 ) :
                mang_cap_cs.append(chi_so_ben_trai)
                mang_cap_cs.append(i)
                chi_so_ben_trai=i
                mang_cac_cap_chi_so.append(mang_cap_cs)
        return mang_cac_cap_chi_so
    for cap in mang_tam(y):
        if cap[1]-cap[0] == 1:
            continue
        else:
            print(cap)
mang_cap_chi_so_khoang_don_dieu(y)

plt.scatter(x[29:77],y[29:77],color='red')
plt.scatter(x[0:14],y[0:14],color='red')
plt.scatter(x[14:29],y[14:29],color='blue')
plt.scatter(x[77:],y[77:],color='blue')
plt.show()

