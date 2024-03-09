import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Đọc dữ liệu
df=pd.read_excel(r'D:\PPS\0.xlsx')
X=df.iloc[:,0]
Y=df.iloc[:,1]
n=len(Y)
#Tạo ma trận vế trái của hệ phương trình
order_4=np.sum(np.sum([pow(x,4) for x in X]))
order_3=np.sum(np.sum([pow(x,3) for x in X]))
order_2=np.sum(np.sum([pow(x,2) for x in X]))
order_1=np.sum(np.sum([pow(x,1) for x in X]))
matrix=[[order_4,order_3,order_2],[order_3,order_2,order_1],[order_2,order_1,n]]
left_matrix=np.array(matrix)
#Tạo ma trận vế phải của hệ phương trình
arr_1,arr_2,arr_3=[],[],[]
for i in range(n):
    arr_1.append(pow(X[i],2)*Y[i])
    arr_2.append(X[i]*Y[i])
    arr_3.append(Y[i])
sum_1=np.sum(arr_1)
sum_2=np.sum(arr_2)
sum_3=np.sum(arr_3)
right_matrix=np.array([[sum_1,sum_2,sum_3]])
result=np.linalg.inv(left_matrix)@right_matrix.T
result=result[:,0]
#Xây dựng hàm bậc 2
def parabol(a,b,c,x):
    return a*pow(x,2)+b*pow(x,1)+c
#Vẽ đồ thị
predict=[]
a=result[0]
b=result[1]
c=result[2]
for value in X:
    predict.append(parabol(a,b,c,value))

plt.plot(X,predict,c='red')
plt.scatter(X,Y)
plt.show()


