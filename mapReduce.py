#map函数
from functools import reduce
import math
def fun1(x):
    return x**3

x=[2,4,6,8,10]
y=map(fun1,x)
print(list(y))

#reduce函数


def fun2(x,y):
    z=x if x>y else y
    return z
x1=[3,5,2,8,10]
y1=reduce(fun2,x1)
print(y1)

#练习 1。使用map函数计算一组已知圆半径的面积

def area(r):
    return math.pi*r*r
a=[3,5,8,10]
b=map(area,a)
print(list(b))


#2.使用reduce()计算6！

def mul(x,y):
    return x*y
c=[1,2,3,4,5,6]
print(reduce(mul,c))
