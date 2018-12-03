#在python中，可以使用try...except语句来处理异常。做法是，把可能引发异常的语句放在try-块中，把处理异常的语句放在except-块中。
try:
    f = open('non-exist.txt')
    print('file opened')
    f.close()
except:
    print('file not exist')
print('done')