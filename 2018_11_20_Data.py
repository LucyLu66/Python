#1.先把文件读进来
f = open('scores.txt', 'r', encoding='UTF-8') #文件中有中文需要进行转换，不然会报错

#2.取得文件中的数据，用readlines获取每一行
lines = f.readlines()
print(lines)
f.close()
results = []
#3.对每条数据进行处理。按照空格，把姓名、成绩分开
for line in str(lines):
    print(line)
    data = line.split()
    print(data)

#4.对于每一条数据，都新建一个字符串，把学生的名字和算好的总成绩保存进去。最后再把这些字符串一起保存到文件中
    sum = 0
    for score in data[1:]:
        sum += int(score)
    result = '%s\t: %d\n' %(data[0: 2], sum)
    print(result)

#5.得到总成绩后，把它添加到list中
    results.append(result)
    print(results)
#6.最后，把results中的内容保存到文件。因为results是一个字符串组成的list，这里我们直接用writelines方法：
output = open('result.txt', 'w')
output.writelines(results)
output.close()

