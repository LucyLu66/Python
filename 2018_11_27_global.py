#在 Python 的函数定义中，可以给变量名前加上 global 关键字，这样其作用域就不再局限在函数块中，而是全局的作用域。
def func():
    global x #函数中的 x 和外部的 x 就成为了同一个变量
    print('beginning func(x):', x)
    x = 2
    print('end func(x):', x)
x = 50
func()
print('after func(x):', x) #当 x 在函数 func 内部被重新赋值后，外部的 x 也随之改变