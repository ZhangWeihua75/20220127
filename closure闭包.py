#闭包：在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。这样就构成了一个闭包。

def price(weight,unitPrice):
    return (weight-0.1)*unitPrice

apple=price(5.1,3)
banana=price(10.1,5)
print("Apple 的价格是：",apple)
print("香蕉的价格是：",banana)

#如果使用闭包

def price1(unitPrice):
    def computer(weight):
        return (weight-0.1)*unitPrice
    return computer

apple1=price1(3) #这里函数不执行，只是进行了一次引用
print(apple1(10.1))

banana1=price1(5)
print(banana1(5.1))

#练习 构造一个闭包程序，能够根据需要计算平方，立方

def pingfang(a):
    def mul(b):
        return b*a
    return mul

a1=pingfang(5)
print(a1(5))

def lifang(c):
    def pf(a):
        return a*a*c
    return pf 

b1=lifang(5)
print(b1(5))