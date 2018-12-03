str1 = 'good'
str2 = 'bye'
print(str1 + str2)
print('very' + str1)
print(str1 + ' and ' + str2)

#字符和数字不能直接相加，需要用str()转化为字符
num = 4
print('I\'m ' + str(num) + ' years old.')

#也可以用%对数字进行格式化
#  %d转化整数    %f转化小数
print('my age is %d' %num)
a = 5.12
print('today is %f' %a)
#保留两位小数用%.2f
print('today is %.2f' %a)


#%s可以用来替换字符串
name = 'Eric'
print('%s is a good man.' %name)

print('-------------------------')
#小游戏改进
num = 20
print('Guess how old am I?')
answer = False
while answer == False:
    age = int(input())
    if age > num:
        print(str(age) + ' is big')
    if age < num:
        print('%d is samll' %age)
    if age == num:
        answer = True
        print('Bingo, '+ str(age) + ' is the right answer')
