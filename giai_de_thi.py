import math
import matplotlib.pyplot as plt
import numpy as np
Z=[-1.14159,-1.23368,-1.2758,-1.27445,-1.23452,-1.15954,-1.05189,-0.54357,-0.3122]
Y=[]
for value in Z:
    Y.append(value+1/15)
def cac_moc_noi_suy_toi_uu(i,a,b):
    return 1/2*((b-a)*math.cos((2*i+1)*math.pi/(2*8+2))+(b+a))
X=[]
for i in range(0,9):
    X.append(cac_moc_noi_suy_toi_uu(i,1,5))

def mau_so(index):
    mau=1
    for i in range(len(X)):
        if i!=index:
            mau*=(X[index]-X[i])
    return mau
def cong_thuc_ns(X):
    danh_sach_mau_so=[]
    for i in range(len(X)):
        danh_sach_mau_so.append(mau_so(i))
    cong_thuc_noi_suy=""
    for j in range(len(danh_sach_mau_so)):
        cong_thuc_noi_suy=""
        yi_mul_Li=""
        for i in range(len(X)):
            if i!=j:
                yi_mul_Li+=f"(x-{X[i]})" 
        cong_thuc_noi_suy+=yi_mul_Li+"/"+f"{danh_sach_mau_so[j]}"
        print(cong_thuc_noi_suy)

moc_noi_suy=[]
for i in range(0,9):
    moc_noi_suy.append(-1+0.25*i)
def bang_sai_phan(Y):
    X=np.zeros((len(Y),len(Y)),float)
    for i in range(len(Y)):
        X[0][i]=Y[i]
    for i in range(1,len(Y)):
        for j in range(len(Y)-i):
            X[i][j]=X[i-1][j+1]-X[i-1][j]
    return X

def giai_thua(n):
    if n==0:
        return 1
    else:
        return n*giai_thua(n-1)
def phi_t(value):
    def ham_tich(value,n):
        output=1
        for i in range(n+1):
            output*=(value-i)
        return output

    result=(value-Y[0])
    for i in range(1,len(Y)-1):
        result-=bang_sai_phan(Y)[i+1][0]*ham_tich(value,i)/math.factorial(i+1)
    return result/bang_sai_phan(Y)[1][0]

def noi_suy_nguoc(value):
    bang_kqua=[(value-Y[0])/bang_sai_phan(Y)[1][0]]
    for i in range(9):
        bang_kqua.append(phi_t(bang_kqua[i]))
    return bang_kqua

plt.scatter(moc_noi_suy,Y)
plt.scatter(-1.25,-4.461118929370708e+70,c='r')
plt.show()

