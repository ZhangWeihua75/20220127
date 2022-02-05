x=[12,45,38,100,789,58,0,999,152,399]
flag=0
for i in x:
    if i==0:
       flag=1
if flag==1:
    print("In the list,there is 0!")       
else:
    print("In the list,there isn't 0!")  
#利用break，可以提前终止循环遍历
print("\n利用break，可以提前终止循环遍历\n")
y=[12,45,38,100,789,58,0,999,152,399]
flag=0
for a in y:
    print(a,end=",")
    if a==0:
       flag=1
       break
       
if flag==1:
    print("\nIn the list,there is 0!")       
else:
    print("\nIn the list,there isn't 0!")       
#利用break，判断列表内是否存在奇数
z=[2,10,14,100,17,18,35,102]    
flag=0
num=1
for b in z:
    print("循环进行了",num,"次")
    if b%2==1:
       flag=1
       break
    num+=1
if flag==1:   
    print("In List,there is odd number!")
else:   
    print("In List,there isn't odd number!")    