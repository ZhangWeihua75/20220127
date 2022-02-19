#构造一个学生类，包含身高体重属性，和学习的方法，构造各类对应得实例“张三”，访问实例的属性和方法

class student:
    def __init__(self,name,height,weight):
        print("Hello,tongxue:")
        self.name=name
        self.height=height
        self.weight=weight
        print("初始化结束")
    def study(self):
        print("我会学习！")
        
student1=student("张三",180,80)
print("我是",student1.name)
print("我的身高是",student1.height,"cm")
print("我的体重是",student1.weight,"kg.")
print(student1.study())
              