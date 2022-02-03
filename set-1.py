#集合不允许重复的值出现
a={2,3,4,6,8,8}
print(type(a))
print(a)
b=[1,2,3,4,5,6]
a1=set(b)
print(a1)
c={22,3,5,21,10}
print(c)
#向集合内添加元素
a.add(12)
print(a)
#删除集合以及集合内的元素
a.pop()  #随机删除集合内的一个元素
print(a)
a.remove(8) #定向删除集合内元素
print(a)
#del a  删除整个集合

#集合的交集&，并集|，差集-
d=a&a1
print(d)
print(a|a1)
print(a-a1)
