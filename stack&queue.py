#队列和堆 要添加一个元素进栈使用append（），要退出一个元素，使用pop（），不需要索引

x=[4,16,2,8,10]
print("x:",x)
x.append(888)
print("x:",x)
x.pop()
print("x:",x)

#队列 需要导入deque
from collections import deque
y=deque([3,5,7,9,10])
print("Queue is:",y)

y.append(666)
print(y)
y.popleft()
print("After pop,y is:",y)

#练习1.构造一个栈，并在其中添加和删除一个元素
#练习1.构造一个队列，并在其中添加和删除一个元素