#1. 假设有一个数列，如何把其中每一个元素都翻倍？
#自己解法
list1 = [1, 2, 3, 4, 5, 6]
list2 = []
for i in list1:
    list2.append(i * 2)
print(list2)

#列表综合解法
list2 = [i * 2 for i in list1]
print(list2)

#map解法
list3 = [1, 2, 3, 4, 5, 6]
def double(x):
    return x * 2
list2 = list(map(double, list3))
print(list2)

list2 = list(map(lambda x: x* 2, list1))
print(list2)

#2. 假设有两个数列，如何求和？
lst_1 = [1,2,3,4,5,6]
lst_2 = [1,3,5,7,9,11]
lst_3 = list(map(lambda x, y: x + y, lst_1, lst_2))
print(lst_3)

#报错TypeError: 'NoneType' object is not callable
lst_3 = list(map(None, lst_1))
lst_4 = list(map(None, lst_1, lst_2))
print(lst_4)