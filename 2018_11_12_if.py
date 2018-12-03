string = input()
if string:
    print ('认真学习！')
print ('-------------------------------')

num = 10
print ('Guess how old am I?')
old = int(input())

if num>old:
    print ('too small')
if num<old:
    print ('too big')
if num==old:
    print ('yes!')
