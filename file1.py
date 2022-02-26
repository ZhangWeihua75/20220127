# with open("file2.txt","r") as f:
#     print(f.name)
#     print(f.mode)
#     print(f.encoding)
#     print(f.closed)
# print(f.closed)    


# with open("file2.txt","r") as f:
#     # x=f.read()
#     # print(x)
#     x1=f.read(4) #只读前四个
#     print(x1)
    
#读取一行    
with open("file2.txt","r") as f:
    x=f.readline()
    print(x,end="")  
    print(x.strip())
#读取多行 列表

with open("file2.txt","r") as f:
    x1=f.readlines()
    print(x1)
    #遍历列表
    for i in x1:
        print(i,end="")
    
# 格式化输出内容
    
from datetime import datetime   
with open("file2.txt","r") as f:
    for line in f.readlines():
        myDate,price=line.split(",")
        # print(myDate)    
        # print(price)
        dt=datetime.strptime(myDate,"%Y/%m/%d")
        price=float(price)
   
        # print(dt,price)
        print("时间是：",str(dt.date()),",","销售额是：",str(price))
        
        