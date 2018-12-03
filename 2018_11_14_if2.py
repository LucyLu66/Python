print('x的坐标是：')
x = int(input())

print('y的坐标是：')
y = int(input())

if x >= 0:
    if y >= 0:
        print('1')
    else:
        print('4')
else:
    if y >= 0:
        print('2')
    else:
        print('3')
