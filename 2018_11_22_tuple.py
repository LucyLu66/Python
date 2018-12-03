postion = (1, 2)
geeks = ('Sheldon', 'Leonard', 'Rajesh', 'Howard')

print(postion[0])
for g in geeks:
    print(g)
print(geeks[1:3])

def get_pos(n):
    return (n/2, n*2)
#根据返回值元组中元素的个数提供变量
x, y = get_pos(50)
print(x)
print(y)
#用一个变量记录返回的元组
pos = get_pos(50)
print(pos[0])
print(pos[1])