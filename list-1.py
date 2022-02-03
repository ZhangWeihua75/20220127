#列表练习
a=[2,8,12,18,3,0,9,10]
b=[]
print("列表a",a)
print("列表b",b)
print("a[2]=",a[2])
a[2]=120
print("重新赋值后a[2]=",a[2])
print("重新赋值后a",a)
#负索引
print("a[-1]=",a[-1])
#切片访问   a[开始：结束：步长]   遵循左闭右开的原则
print(a[2:6:2])
print(a[:6])
print(a[6:])
print(a[6:-1]) #不包含-1
#列表的添加append()函数
a.append(888)
print(a)
#删除列表成员
del a[2]
print(a)
#列表练习题 构造一个10个元素的列表，获取列表最后五个值，在列表内增加一个888，删除列表最后一个值

l=[1,3,5,7,9,11,13,15,17,19]
print(l)
print(l[5:])
l.append(888)
print(l)
del l[-1]
print(l)