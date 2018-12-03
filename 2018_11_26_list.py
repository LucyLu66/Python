list_1 = [1, 2, 3, 5, 8, 13, 22]
list_2 = []
for i in list_1:
    if i % 2 == 0:
        list_2.append(i)
#print(list_2)

#使用列表解析实现同样的效果
list_2 = [i for i in list_1 if i % 2 == 0]
print(list_2)

#WORK
#用一行 Python 代码实现：把1到100的整数里，能被2、3、5整除的数取出，以分号（;）分隔的形式输出。
num = range(1, 101)
for i in num:
    list3 = list(num)
#print(list3)
list4 = [i for i in list3 if i % 2 == 0 and i % 3 == 0 and i % 5 == 0]
new = ';'.join(str(list4))
print(new)

#正确解法：
print(';'.join([str(i) for i in range(1,101) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0]))


