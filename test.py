#Work
#从一个文件中读取内容，保存到另一个文件
data = open('test.txt')
one = data.read() #读出第一个文件内容
print(one) #输出第一个文件的内容
data2 = open('file.txt', 'w')
data2.write(one)
data.close()
data2.close()