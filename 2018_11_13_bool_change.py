a = bool('Flase')
print(a)
b = bool(0)
print(b)


#在python中，以下类型转换成bool时，会被认定为False:
   #为0的数字，包括0，0.0
   #空字符串，包括''，""
   #表示空值的None
   #空集合，包括()，[]，{}
#其他的值都认为是True。

a = '123'
if a:
    print('blank string')