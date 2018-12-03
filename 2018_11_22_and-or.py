#在一个bool and a or b语句中，当bool条件为真时，结果是a；当bool条件为假时，结果是b。
a = "heaven"
b = "hell"
c = True and a or b
print(c)
d = False and a or b
print(d)

#有了它，原本需要一个if-else语句表述的逻辑：
#if a > 0:
#    print('big')
#else:
#    print('small')

#就可以直接写成：
#print (a > 0) and "big" or "small"

#and-or真正的技巧在于，确保a的值不会为假。最常用的方式是使 a 成为 [a] 、 b 成为 [b]，然后使用返回值列表的第一个元素：
a = ''
b = 'hell'
c = (True and [a] or [b])[0]
print(c)