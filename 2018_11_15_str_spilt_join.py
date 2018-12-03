sentence = 'It\'s a sentence.'

#字符串分割，以空格进行分割，最终组成一个list
sentence.split()
print(sentence.split())

#join连接字符
s = ';'
li = ['apple', 'pear', 'orange']
fruit = s.join(li)
print(fruit)


word = 'hello world'
#遍历 通过for..in
for c in word:
    print(c)
#索引访问
print(word[0])
print(word[-2])
#切片
print(word[1:5])
print(word[:-3])
print(word[:])
#连接字符
new = ','.join(word)
print(new)
