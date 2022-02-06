
'''
def area1():     #无参数，无返回值
    print(3.14*10*10)
def area2(r):    #有参数，有返回值
    return 3.14*r*r   
def area3():     #无参数，有返回值
    return 3.14*10*10
def area4(r):    #有参数，无返回值
    print(3.14*r*r)
area1()  
print(area2(5))
print(area3())
area4(10)
'''
#定义函数，根据正方形的周长，计算正方形面积
def areaC(l):
    return l*l
print("Surface of squar is:",areaC(5))
