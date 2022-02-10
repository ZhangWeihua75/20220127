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

t=re.compile("[0-9]")
z="我买了2斤苹果，3斤李子。"
print(r.split(z))
#使用句号进行分割
p=re.compile("[，。]")
phar="我的写作目标是内容完整、脉络清晰、通俗易懂，帮助初学者看清技术路径，快速入门。难度为入门级，不涉及深入的细节，重在理解各种技术想要解决的问题，掌握基本用法，为进一步自学打下基础。"
print(p.split(phar))