#输入年龄，判断所处阶段
a=input("Please input your age:")
age=int(a)
if age<18:
    print("Your are child or teenager.")
elif 18<=age<60:
    print("Your are adult.") 
else:
    print("Your are so old!")    