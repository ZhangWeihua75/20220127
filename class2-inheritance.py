#继承inheritance

class people:
    def talk(self):
        print("Hello World!")

class teacher(people):
    def teach(self):
        print("上课了，同学们！")
class student(people):
    def study(self):
        print("开始学习了！")     
class police(people):
    def catch(self):
        print("别动，否则我要开枪了！")    

p1=people()
p1.talk()

t1=teacher()
t1.talk() 
t1.teach()  

p1=police()
p1.catch()            