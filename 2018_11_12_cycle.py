#输出5个*
for i in range(0, 5):
    print('*')

for a in range(0, 5):
    print('*', end = '')#输出的*在同一行
print('\n')

print('输出五行')
for i in range(0, 5):
    for j in range(0, 5):
       print('*', end = '')
    print('\n')
    
print('输出直角三角形')
for i in range(0, 5):
    for j in range(0, i+1):
       print('*', end = '')
    print('\n')

print('输出三角形')
for i in range(1,6):

    for j in range(5-i):

        print(" ",end="")

    for j in range(1,2*i):

        print("*",end="")

    print("\n")
