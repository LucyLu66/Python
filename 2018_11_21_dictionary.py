#字典基本格式是（key是键，value是值）
#d = {key1 : value1, key2 : value2 }

#关于字典的键要注意的是：
#1.键必须是唯一的；
#2.键只能是简单对象，比如字符串、整数、浮点数、bool值。
#list就不能作为键，但是可以作为值。

score = {
    '萧峰': 95,
    '段誉': 97,
    '虚竹': 89
}
print(score['段誉'])

#另一种get方法，提供的键不存在，也不会报错，只会返回 None
print(score.get('虚竹'))

#for...in遍历,遍历的变量中存储的是字典的键。
for name in score:
    print(score[name])

#改变键的值
score['萧峰'] = 100
print(score['萧峰'])

#增加字典项，给新键赋值
score['张三'] = 99
print(score['张三'])

#删除字典项
del score['段誉']
print(score.get('段誉')) #删除成功，输出None

#建一个空字典
d = {}
