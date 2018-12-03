class Myclass:
    pass
mc =  Myclass()
print(mc)

#给类加上域
class Myclass:
    name = 'Sam' #增加了一个类变量name
    def sayHi(self): #类方法
        print('Hello %s' %self.name)
mc = Myclass() #新键一个对象的实例mc
#调用类变量的方法是“对象.变量名”
print(mc.name)
mc.name = 'Lucy' #修改类变量的值
print(mc.sayHi()) #通过“对象.方法名()”格式进行调用

