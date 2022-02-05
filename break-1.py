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