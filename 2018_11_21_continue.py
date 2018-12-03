#break是彻底地跳出循环，而continue只是略过本次循环的余下内容，直接进入下一次循环。

i = 0
while i < 5:
    i += 1
    for j in range(3):
        print(j)
        if j == 2:
            break
    for k in range(3):
        if k == 2:
            continue
        #print(k)
    if i > 3:
        break
    #print(i)


