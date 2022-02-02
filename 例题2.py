#比较运算符
a=5
b=4
print(a<b)
print(a==b)  #用==判断是否相等
print(a!=b)  # 用！=表示不相等

#类型转换

a1="5"
b1="4"
print("Type(a1)=",type(a1))
ia1=int(a1)
print("ia1的类型是",type(ia1))
c1="6"
fc1=float(c1)
print(fc1)

a2="圆周率是："
b2=3.14
print(a2+str(b2))
print(a2+repr(b2))
print(repr(a2+repr(b2)))  #repr可以给字符串加上单引号，也可以实现转换成字符串的功能

#计算”4+6“，用类型转换的功能，分别使其结果是46和10
s1="4"
s2="6"
print("4+6=",s1+s2)
print("4+6=",int(s1)+int(s2))
