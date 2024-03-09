import matplotlib.pyplot as plt


def khoi_tao(left,right,h):
    x=[]
    n=int((right-left)/h)
    for i in range(n+1):
        x.append(left+i*h)
    return x


def f(x,y):
    return (x+2*y)/(x**2+2*y**2)

x=khoi_tao(0,1000,0.1)
y=[]
y.append(1)

#Tính 4 nút lưới đầu tiên bằng Euler hiện
for i in range(1,4):
    y.append(y[i-1]+0.1*f(x[i-1],y[i-1]))

#Tính các mốc còn lại bằng AB4-AM4
#B1:Tính bằng AB4
def cong_thuc_AB4(Y_last,h,y_phay_i,y_phay_i_1,y_phay_i_2,y_phay_i_3):
    return Y_last+h/24*(55*y_phay_i-59*y_phay_i_1+37*y_phay_i_2-9*y_phay_i_3)
for i in range(4,10001):
    y.append(cong_thuc_AB4(y[i-1],0.1,f(x[i-1],y[i-1]),f(x[i-2],y[i-2]),f(x[i-3],y[i-3]),f(x[i-4],y[i-4])))

def cong_thuc_AM4(Y_last,h,y_phay_i1,y_phay_i,y_phay_i_1,y_phay_i_2):
    return Y_last+h/24*(9*y_phay_i1+19*y_phay_i-5*y_phay_i_1+y_phay_i_2)
#B2:Hiệu chỉnh lại các giá trị của y
for i in range(4,10001):
    y[i]=cong_thuc_AM4(y[i-1],0.1,f(x[i],y[i]),f(x[i-1],y[i-1]),f(x[i-2],y[i-2]),f(x[i-3],y[i-3]))
#B3:Vẽ đồ thị
plt.plot(x,y)
plt.show()
