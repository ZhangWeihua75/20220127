#输出100以内的所有奇数
print("100以内的所有奇数:")
x=1
while x<100:
    if x%2==1:
        print(x,end=",")
    x+=1
print("\n利用步长来解决：")    
x=1
while x<100:
    print(x,end=",")
    x+=2
print("\n")

#空值案例，输入你的名字，输出hello，
name=""
while not name:
    name=input("Please input your name:")
print("Hello",name)       

#练习，输出1-100以内所有能被13整除的数
print("\n1-100以内能被13整除的数：")
i=1
while i<100:
    if i%13==0:
        print(i,end=",")
    i+=1