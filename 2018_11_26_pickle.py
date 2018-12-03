import pickle
data = ['hello', 613, True]
file = open('test.txt', 'wb+') #python3中，通过pickle对数据进行存储时，必须用二进制(b)模式读写文件。
pickle.dump(data, file)
file.close()

file = open('test.txt', 'r', encoding='UTF-8')
data = pickle.load(file)
file.close()
print(data)