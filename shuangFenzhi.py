#判断输入的数是否是偶数
a=input("Please input an integer number:")
a1=int(a)
if a1%2==0:
     print(a1,"是一个偶数！")
else:
     print(a1,"是一个奇数！")     
     
#输入您的考试成绩，判断是否及格
score=input("Please input your score:")
if int(score)>=60:
    print("你的成绩已经及格！")
else:
    print("没有及格，请继续学习，准备补考吧！")     