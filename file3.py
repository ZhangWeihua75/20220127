#存储文件
file="file4.txt"
with open(file,mode="w") as f:
    f.write("888888")
    print(f.read())
    
x=open("file2.txt","r")
y=open("zwh.txt","w" )

y.writelines(x.readlines())
x.close()
y.close()
