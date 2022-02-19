#封装 Encapsulation
class person:
    def __init__(self,name,age):
        print("--初始化开始--")
        self.name=name
        self.age=age
        print("--初始化结束--")
    def show(self):  #封装了
        print("我是",self.name)
        print("我的年龄是",self.age)
p1=person("张三",45)
p1.show()

#构造一个类，能够显示其中的所有属性attribute

class computer:
    def __init__(self,model,Cpu,Ram,Harddisk,Hdmi):
        print("--Comuter initial--")
        self.model=model
        self.Cpu=Cpu
        self.Ram=Ram
        self.Harddisk=Harddisk
        self.Hdmi=Hdmi
        print("--Initial end!")
    def show(self):
        print("Model:",self.model)
        print("CPU:",self.Cpu)    
        print("RAM:",self.Ram)
        print("HARDDISK:",self.Harddisk)
        print("HDMI NUMBERS:",self.Hdmi)
c1=computer("IBM ThinkPad R2500","I7 3455","4G","2T",2)        
c1.show()