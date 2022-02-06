import os,sys,time,math

print(os.getcwd())   #get current working directory

print(sys.argv)      #show current working file
print(sys.platform)  
print(sys.path)

#计算程序运行时间
start=time.time()
for i in range(1000000):
     i+=1
end=time.time()     
print("程序运行了",end-start,"秒")

print("Program start:")
time.sleep(5)
print("Program end!")

print(time.localtime())

# Math function
print(math.sin(math.pi/2))
print(math.cos(math.pi/2))
print(math.tan(math.pi/2))


