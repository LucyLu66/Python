#得到程序开始和结束所用的时间，进而算出运行的时间
import time
start =time.time()
print('starttime:%f' %start)
for i in range(10):
    print(i)
end = time.time()
print('endtime:%f' %end)
print('total time:%f' %(end - start))

#time.sleep(secs),它可以让程序暂停secs秒。
print(1)
time.sleep(3) #输出1之后休息3秒输出2
print(2)