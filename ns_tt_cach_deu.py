import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel(r"C:\Users\NTCUONG\Downloads\0.xlsx")
X=list(df.iloc[:,0])
Y=list(df.iloc[:,1])

value=float(input("NHAP x : "))

