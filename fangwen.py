#访问控制 get set
class people:
    def __init__(self,name,age):
       self.name=name
       self.__age=age
    def show(self):
        print("我的名字是：",self.name)
        print("我的年龄是：",self.__age)
    def setage(self,age):
        if age<0:
            print("年龄不符合要求！")
        else:
            self.__age=age
    def getage(self):
        return self.__age       
 
zwh=people("张三",18)   

zwh.show()    

zwh.setage(45)
zwh.show()
print(zwh.getage())        