# from 模块名 import 方法名

from random import randint

num = randint(1,50)

print ('Guess how old am I?')
answer = False
while answer==False:
    old = int(input())
    if old > num:
        print ('big')
    if old < num:
        print ('small')
    if old == num:
        answer = True
        print ('yes!')

#为了便于理解和避免冲突，你还可以给引入的方法换个名字
from math import pi as math_pi #将方法名pi改为math_pi
print(math_pi)

