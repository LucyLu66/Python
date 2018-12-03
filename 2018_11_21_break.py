while True:
    a = input()
    if a == 'off':
        break

#下面的程序接受用户3次输入，当用户输入一行“off”时，程序提前结束。
for i in range(3):
    a = input()
    if a == 'off':
        break

#猜数字游戏：加上break功能，当猜到负数时，提前结束游戏
def isEqual(num1, num2):
    if num1 > num2:
        print('too big')
    else:
        if num < 0:
            print('退出游戏')
        else:
            print('too small')
    if num1 == num2:
        print('bingo')

from random import randint
num = randint(1,100)
print('Guess how old am I?')
bingo = False
while bingo == False:
    age = int(input())
    isEqual(age, num)
    if age < 0: #当猜到负数时，提前结束游戏
        break

