def sum(a, b, c):
    return a + b + c
print(sum(1, 2, 3))
print(sum(4, 5, 6))

#使用 lambda 表达式来实现:lambda 参数列表: 表达式
sum = lambda a, b, c: a + b + c
print(sum(1, 2, 3))
print(sum(4, 5, 6))

#把 lambda 表达式用在 def 函数定义中
def fn(x):
    return lambda y: x + y #函数的返回值是一个 lambda 表达式
a = fn(2) #相当于：a = lambda y: 2 + y
print(a(3))
