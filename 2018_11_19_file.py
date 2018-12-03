txt = open('file.txt')
#读出文件内容
data = txt.read()
print(data)
txt.close()

#读取一行内容
txt = open('file.txt')
one = txt.readline()
print(one)
txt.close()

#把内容按行读取至一个list中
txt = open('file.txt')
two = txt.readlines()
print(two)
txt.close()

#'w'就是writing，以这种模式打开文件，原来文件中的内容会被你新写入的内容覆盖掉，如果文件不存在，会自动创建文件。
f = open('test.txt', 'w')
data1 = f.write('that\'s right')


data = 'I will be in a file.\nSo cool!'
out = open('output.txt', 'w')
out.write(data)
out.close()

#还有一种模式是'a'，appending。它也是一种写入模式，但你写入的内容不会覆盖之前的内容，而是添加到文件中。


