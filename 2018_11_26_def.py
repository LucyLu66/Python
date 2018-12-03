def func(arg1, arg2):
    print(arg1, arg2)
func(3, 7)

def func2(arg1 = 3, arg2 = 7):
    print(arg1, arg2)
func2()

#func(a=1, b=2, c=3)
def func3(arg1 = 3, arg2 = 7, arg3 = 5):
    print(arg1, arg2, arg3)
func3() #输出默认值
func3(2, 3, 4) #重新指定三个参数的值
func3(5, 6) #重新指定1、2参数的值
func3(10) #重新指定第一个参数的值

#也可以指定其中的部分参数
func3(arg2=60)
#混合起来用
func3(23, arg3=15)

#def func(*args),它可以接受任意数量的参数.
def Sum(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)
Sum(1, 2, 3, 4)
Sum(1, 2)
Sum()

#变量前加上星号前缀（*），调用时的参数会存储在一个 tuple（元组）,tuple 是有序的，所以 args 中元素的顺序受到赋值时的影响。
def printAll(*args):
    for i in args:
        print(i)
printAll(1, 2, 3)
printAll(3, 2, 1)

#func(**kargs),把参数以键值对字典的形式传入。
def printA(**kwargs):
    for k in kwargs:
        print(k, ':', kwargs[k])
printA(a = 1, b = 2, c = 3)
printA(x = 4, y =5)

#三种调用方式混合使用
def func4(x, y=5, *a, **b):
	print(x, y, a, b)

func4(1)
func4(1,2)
func4(1,2,3)
func4(1,2,3,4)
func4(x=1)
func4(x=1,y=1)
func4(x=1,y=1,a=1)
func4(x=1,y=1,a=1,b=1)
func4(1,y=1)
func4(1,2,3,4,a=1)
func4(1,2,3,4,k=1,t=2,o=3)