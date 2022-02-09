import random
a=random.randrange(1,20,3)
print(a)

print(random.randint(1,10))  #include 10

# random.choice() 
x=["CSDN","Olympia","Hello","Bye-Bye"]
print(random.choice(x))

y=range(50)
z=list(y)
print("z:",z)
random.shuffle(z)  #shuffle()的返回值是个NONE,只是将列表中的数据进行操作
print("z:",z)

#random.sample() 取样
l=["Alice","Allen","Leo","Lily"]
print(random.sample(l,2))

#生成一个100-200之间的随机偶数
print(random.randrange(100,200,2))

#讲1-100之间的数随机排列
c=range(100)
c1=list(c)
random.shuffle(c1) #操作的对象是LIST（C1的值）
print(c1)

#uniform(a,b))产生一个ab之间的随机数
print(random.uniform(9,10))
print(random.random())#产生0---1之间的一个随机数
