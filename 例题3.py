n=3
s="土豆"
print("我买了",n,"斤",s)

#占位符的使用
print("我买了%s斤%s" %(n,s))
print("我买了{}斤{}".format(n,s))

#排错
aa=input("请输入一个数值")
print("Result=",int(aa)+2)
print(aa*2)

#课后作业 分别输入a5=4和b5=6,让其结果是46 和10
a5=input("请输入数值1:")
b5=input("请输入数值2:")
print("a5+b5=",a5+b5)
print("a5+b5=",int(a5)+int(b5))


