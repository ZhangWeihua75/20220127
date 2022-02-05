#利用while遍历
a=[2,4,34,100,120]
i=0
while i<len(a):
    if i!=len(a)-1:
       print(a[i],end=",")
    else:
       print(a[i]) 
    i+=1
#奇数偶数案例
x=[23,12,15,8,19,100,231,240,1000]    
even=[]
odd=[]
i=0
while i<len(x):
      if x[i]%2==0:
          even.append(x[i])
      else:
          odd.append(x[i]) 
      i+=1
print("even list:",even)  
print("\nodd list:",odd) 

#利用pop（）
y=[28,12,17,8,33,102,230,240,1001]    
evenL=[]
oddL=[]
while len(y)>0:
      n=y.pop()
      if n%2==0:
          evenL.append(n)
      else:
          oddL.append(n) 
print("even list:",evenL)  
print("\nodd list:",oddL)          
#计算一个列表内，奇数和偶数的个数
z=[4,9,15,8,100,131,150]
i=0
eNum=0
oNum=0
while i<len(z):
    if z[i]%2==0:
       eNum+=1
    else:
        oNum+=1
    i+=1    
print("Ever number is:",eNum) 
print("\nOdd number is:",oNum)                 