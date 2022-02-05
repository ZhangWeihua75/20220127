a=range(1,10,3)
b=list(a)
print("List b=",b)
a1=range(1,5)
print(type(a1))
print(list(a1))
a2=range(10)
print(list(a2))
#range函数产生一个可迭代的对象
for x in range(1,6):
      print(x,"loop")
#计算1-100的和
s=0
for i in range(1,101):
     s+=i
print("The sum of 1-100 is:",s)     
#使用函数的方式，计算1-100的和
print(sum(range(1,101)))
#输出1-100的所有奇数
print("The odd numbers of 1 to 100:")
#通过利用步长来实现
print("通过利用步长来实现")
for i in range(1,100,2):
    print(i,end=",")
print("通过利用选择结构来实现")  
for i in range(1,101):
    if i%2!=0:
        print(i,end="-")
print('\n')        
#练习，请打印出1-100之间所有能被7整除的数
for i in range(1,101):
    if i%7==0:
        print(i,end=",")
     