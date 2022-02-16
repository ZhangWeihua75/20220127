#迭代器 iter()
x=["zwh","python","lesson"]
y=iter(x)
print(next(y))
print(next(y))
print(next(y))

#生成器 gen()
def gen(n):
    for i in range(n):
        yield i*i

x=gen(5)
for i in x:
    print(i,end=" ")  
print("\n")    
#简化后的生成器
gen=(i*i for i in range(5))
for i in gen:
    print(i,end=" ") 

#为什么使用生成器
import sys,time

t1=time.time()             
mylist=[i for i in range(10000000)]
t2=time.time()
print("占用时间",t2-t1)
print("占用空间",sys.getsizeof(mylist)) #存储的是数据

#使用生成器
t3=time.time()             
mygen=(i for i in range(10000000))
t4=time.time()
print("占用时间",t4-t3)
print("占用空间",sys.getsizeof(mygen))#存储的是公式，所以占用资源小

#构造一个计算绝对值的生成器



    
    