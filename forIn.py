#利用 for in 来遍历列表
a=[2,3,6,9,82,100]
for x in a:
    print(x)
#利用 for in 来遍历元组
b=("tom","csdn","python") 
for a,b in enumerate(b):
     print(a,b) 
#利用 for in 来遍历字典
x={
    "leo":5,
    "lily":8,
    "andy":11,
    "me":18
}       
for a,b in x.items():
     print(a,b)
print("=======keys======")    
for a in x.keys():
     print(a)
print("=======values======")    
for a in x.values():
     print(a)     
     
#利用 for in 来遍字符串
s="PYTHON"
print("======string=======")
for a in s:
     print(a)    
for b in s:
     print(b,end="-")       
#构造一个列表由正数，负数和零组成，利用FOR IN遍历列表，将正数输出
print("\n构造一个列表由正数，负数和零组成，利用FOR IN遍历列表，将正数输出")
list1=[22,-3,0,12,-1,9,8,-2,100,10]
print("列表：",list1)
print("其中正数包括：")
for a in list1:
    if a>0:
         print(a,end=",")
         


     