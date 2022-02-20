#多态 polymorphism
#1.构造一个基类“学生”，包含学习的方法2.构造继承类“计算机专业学生，重新实现方法”学习“。3.构造继承类“金融专业学生，重新实现方法”学习“
#4构造一个函数“fun"，能够调用基类“学生”的方法。5.构造不同类的对象，将其作为函数fun的参数

class student:
    def study(self):
        print("我在学习")

class csStudent(student):
     def study(self):
        print("我在学习Python")         
class finStudent(student):
     def study(self):
        print("我在学习财务分析")   
        
def startStudy(student):
     print("----学生说----") 
     student.study() 
       
s1=student()
s1.study()  

cs1=csStudent()      
cs1.study()
fin1=finStudent()
fin1.study()

startStudy(s1)
startStudy(cs1)
startStudy(fin1)

print(isinstance(cs1,student))

