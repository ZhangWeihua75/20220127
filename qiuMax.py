
#输入两个数值，利用条件语句，输出最大值
'''
x=input("请输入数值x:")
y=input("请输入数值y:")
z=int(x)
if z<int(y):
     z=int(y)
print("Max number of the two numbers entered is:",z)
'''
'''
#输入两个数字，按照从小到大的排序顺序输出
a=input("Please input number 1:")
b=input("Please input number 2:")
a1=int(a)
b1=int(b)
if a1>b1:
     c=a1
     a1=b1
     b1=c
print("After sorted:",a1,b1)     
'''
'''
#python的方法进行数据交换
a2=input("Please input number 1:")
b2=input("Please input number 2:")
a22=int(a2)
b22=int(b2)
if a22>b22:
    a22,b22=b22,a22
print(a22,b22)    
'''
#计算4个数中的最大值
a=input("Please input number 1:")
b=input("Please input number 2:")
c=input("Please input number 3:")
d=input("Please input number 4:")
a1=int(a)
b1=int(b)
c1=int(c)
d1=int(d)
print("The four numbers you entered are:",a1,b1,c1,d1)
if a1<b1:
      t=a1
      a1=b1
      b1=t
print("Max of a1 and b1:",a1)      
if c1<d1:
      l=c1
      c1=d1
      d1=l
print("Max of c1 and d1:",c1)        
if a1<c1:
     print("The max number is:",c1)     
else:
      print("The max number is:",a1)    
