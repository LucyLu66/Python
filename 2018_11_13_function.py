#定义函数关键字def

def sayHello():
    print('hello world!')
sayHello()
sayHello() #可重复调用

def hello(name):
    print(name + 'good morning!')

#多个参数可以用,号隔开
def socre(num1, num2):
    print(num1 + num2)

hello('lucy ')
socre(12, 15)

#也可以传入变量
x = 3
y = 4
socre(x, y)

def isEqual(num1, num2):
    if num1 < num2:
        print('too small')
        return False
    if num1 > num2:
        print('too big')
        return False
    if num1 == num2:
        print('Bingo')
        return True
isEqual(3, 6)

#优化小游戏
from random import randint
num = randint(1, 100)
print('Guess how old am I?')
answer = False
while answer == False:
    age = int(input())
    answer = isEqual(age, num)