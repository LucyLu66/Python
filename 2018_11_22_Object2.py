#假设我们有一辆汽车，我们知道它的速度(60km/h)，以及A、B两地的距离(100km)。要算出开着这辆车从A地到B地花费的时间。（很像小学数学题是吧？）

#面向过程的方法
speed = 60.0
distance = 100.0
time = distance/speed
print(time)

#面向对象的方法
class Car:
    speed = 0 #指定类变量
    def drive(self, distance): #指定类方法
        time = distance/self.speed
        print(time)
car = Car() #指定car为对象
car.speed = 60.0 #给类变量赋值
car.drive(100.0) #给类方法赋值

#假设我们又有了一辆更好的跑车，它的速度是150km/h，然后我们除了想从A到B，还要从B到C（距离200km）。要求分别知道这两种车在这两段路上需要多少时间。

car1 = Car()
car1.speed = 60.0
car1.drive(100.0)
car1.drive(200.0)

car2 = Car()
car2.speed = 150.0
car2.drive(100.0)
car2.drive(200.0)
