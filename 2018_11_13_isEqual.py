def isEqual(num1, num2):
    if num1 < num2:
        print('too small')
        return False
    elif num1 > num2:
        print('too big')
        return False
    else:
        print('Bingo')
        return True

from random import randint
num = randint(1, 100)
print('Guess how old am I?')
bingo = False
while bingo == False:
    answer = int(input())
    isEqual(answer, num)
