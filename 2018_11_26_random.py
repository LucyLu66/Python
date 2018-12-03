#random.randint(a, b)可以生成一个a到b间的随机整数，包括a和b。
#a、b都必须是整数，且必须b≥a
import random
num = random.randint(1, 100)

#当a,b相等的时候，结果永远是一个数
num = random.randint(3, 3)

#random.random(),生成一个0到1之间的随机浮点数，包括0但不包括1，也就是[0.0, 1.0)。
num = random.random()

#random.uniform(a, b),生成a、b之间的随机浮点数。不过与randint不同的是，a、b无需是整数，也不用考虑大小。
num = random.uniform(9, 1.5)
num = random.uniform(1.5, 9)
num = random.uniform(1.5, 1.5) #永远得到1.5

#random.choice(seq)，从序列中随机选取一个元素。seq需要是一个序列，比如list、元组、字符串。
num = random.choice([1, 3, 5, 7, 8]) #list
num = random.choice('lucy') #字符串
num = random.choice(['hello', 'word','hi']) #字符串组成的list
num = random.choice((1, 2, 3, 4, 5)) #元组

#random.randrange(start, stop, step)，生成一个从start到stop（不包括stop），间隔为step的一个随机数。
# start、stop、step都要为整数，且start<stop。
num = random.randrange(1, 9, 3)
#start和step都可以不提供参数，默认是从0开始，间隔为1。但如果需要指定step，则必须指定start。
num = random.randrange(4) ##[0, 1, 2, 3]
num = random.randrange(1, 4) #[1, 2, 3]

#random.randrange(start, stop, step)其实在效果上等同于random.choice(range(start, stop, step))
num = random.choice(range(1, 9, 3))

#random.sample(population, k),从population序列中，随机获取k个元素，生成一个新序列。sample不改变原来序列
str = {
    'kjdsfkj',
    123,
    'lucy',
    5.20
}
num = random.sample(str, 2)

#random.shuffle(x),把序列x中的元素顺序打乱。shuffle直接改变原有的序列。
str1 = ['lucy', 123, 'eric', 5.20]
num = random.shuffle(str1)

print(num)
