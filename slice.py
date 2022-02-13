#切片的访问，以List为例
x=[2,12,111,34,56,19,1200,100,0,1]
#单个元素的访问
print(x[0])
print(x[-2])
#整个切片的访问
print(x[:])
print(x[::])
#逆序访问
print(x[::-1]) 

#多层切片
print(x[2:6])
print(x[2:6][1:3])
print(x[2:6][1:3][-1])

#利用步长可以进行奇数或偶数位置的索引
print(x[::2]) #奇数位置
print(x[1::2]) #偶数位置

#插入元素
y=[2,4,6,8,9]
print(y)
y[5:]=[10,12,14]
print(y)
#头部添加
y[:0]=[22,34,12]
print(y)
#中间插入
y[2:2]=[55,66]
print(y)
#替换元素
y[2:4]=[88,99]
print(y)
#替换不相邻位置，此时左右的长度要一致
y[1::2]=[0,0,0,0,0,0]
print(y)
#删除元素
y[:2]=[] #删除前两个元素
print(y)
y[5:]=[] #删除5以后的元素
print(y)

#利用del删除元素

del y[::2]
print(y)

#练习  构造一个字符串，利用不同的方式，取到其最后3个字符
str="Hello World!"
print(str)
print(len(str))
print(str[len(str)-3:])
print(str[-3:])
s=str[-3:]
print(s)