#z正则表达式 Regluar Expression

from distutils.filelist import findall
import re

x="ZWH的Python课程，在CSDN的课程。"
print(re.search("，",x))

print(re.match("ZWH",x))
print(re.split("P",x))
print(re.findall("n",x))
print(re.findall("[nNP]",x))

r=re.compile("[0-9]")
y="今天是2022年2月8日！"

print(r.search(y))
print(r.findall(y))
print(r.match(y))
s=re.compile("[是]")
print(s.split(y))