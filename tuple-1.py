#元组Tuple练习 Python的元组与列表类似，不同之处在于元组的元素不能修改。

#元组使用小括号，列表使用方括号。

#元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

a=(2,4,6,3,12,10,8,5,110,99)
print(type(a))
print(a)
print(a[2])
print(a[3:8:2])
print(a[:5])
#删除元组
#del a
#print(a)
#元组的连接

b=(111,112,113)
c=a+b
print("元组c",c)
#元组的长度
l=len(c)
print("Length c=",l)
#元组的迭代* 就是重复元组的值
d=(2,4,6)
print(d*3)


