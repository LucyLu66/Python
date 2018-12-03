
print(list(range(1, 8)))

num = range(1, 3)
for i in num:
    print(list(num))

#可以自己定义列表的值
I = [1, 2, 3, 4]
print(I)

#可以用for..in..遍历这个表
I = ['meat', 'egg', 'fish', 'milk']
for i in I:
    print(i)

#访问list中的元素
print(I[2])

#修改list中的元素
I[0] = 888
print(I)  #list中第一个元素被修改为888

#删除list中的元素
del I[1]
print(I) #删除list中第二个元素

#向list中增加元素
I.append(520)
print(I)  #添加元素520在最后

#罚球小游戏
from random import choice
print('Choose one side to shoot:')
print('left, center, right')

you = input()
print('you kicked ' + you)

dir = ['left', 'center', 'right']
com = choice(dir)   #随机选一个
print('computer saved ' + com)

if you != com: #判断输入的和电脑随机选的是否一样
    print('goal!')
else:
    print('Oops...')
