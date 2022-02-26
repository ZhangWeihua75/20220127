#存储文件
file="file4.txt"
with open(file,mode="w") as f:
    f.write("张三888888")
    print(f.read())