#堆
import heapq
x=[3,9,12,0,5,8,22,100,1,18]
print(x)
heapq.heapify(x)
print(x)

#放入一个元素进堆
heapq.heappush(x,4)
print(x)

#弹出一个元素出堆
heapq.heappop(x)
print(x)

y=[2,5,7,9,12,34,6,100]
print(y)
heapq.heapify(y)
print(y)
z=heapq.heappushpop(y,10) #将item 10放入堆中，并弹出堆中的最小元素 2，堆大小保持不变，先放进去，再弹出来
print("z:",z)
print("y:",y)

#heapreplace()是先弹出堆中最小元素，再放进去一个
w=heapq.heapreplace(y,8)
print("w:",w)
print("y:",y)

#merge()合并两个列表变成一个堆
a=[2,5,7,3,8]
b=[1,3,6,100]
c=heapq.merge(a,b)
print(list(c))

#nsmallest 和nlargest

print("前三个最大值：",heapq.nlargest(3,y))
print("前两个最小值：",heapq.nsmallest(2,y))

#练习 构造一个堆，删除其中最小值，再添加一个值
m=[5,3,6,8,10,24]
heapq.heapify(m)
print("m:",m)
sm=heapq.nsmallest(1,m)
print("The smallest value is:",sm)

heapq.heapreplace(m,9)
print("Now m is:",m)