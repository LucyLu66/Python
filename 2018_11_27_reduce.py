#求1累加到100的和
from functools import reduce #在Python 3里,reduce()函数已经被从全局名字空间里移除了,它现在被放置在fucntools模块里 用的话要 先引入
lst = range(1, 101)
def add(x, y):
    return x + y
print(reduce(add, lst))

#用 lambda 函数
print(reduce(lambda x, y:x + y,range(1, 101)))

