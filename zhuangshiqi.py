#修饰器，即可以有返回值，也可以没有返回值，样式是多种多样的

def zhuangshiqi(function):
    def wrapper(*args,**kwargs):
        print("==========")
        x=function(*args,**kwargs)
        print(x)
        print("----------")
        return x
    return wrapper

@zhuangshiqi
def add(a,b):
    return a+b
@zhuangshiqi
def sub(a,b):
    return a-b
@zhuangshiqi
def add3(a,b,c):
    return a+b+c
@zhuangshiqi
def mul(a,b):
    return a*b
@zhuangshiqi
def div(a,b):
    return a/b

#print(add(3,5))
#print(add3(3,5,6))
#print(sub(8,3))
#print(mul(8,9))

add(3,5)
add3(3,5,6)
sub(8,3)
mul(8,9)

#练习 设计一个装饰器，可以计算圆的面积和正方形的面积
import math

def xiushiqi(function):
    def wrapper(*args,**kwargs):
        print("----The area is----")
        x=function(*args,**kwargs)
        print(x) 
        print("========")
        return x
    return wrapper

@xiushiqi
def cirArea(r):
    return math.pi*r*r
@xiushiqi
def squareArea(l):
    return l*l

cirArea(10)
squareArea(10)





