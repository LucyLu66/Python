num = 10
print ('Guess how old am I?')
old = int(input())

result = old>num
print ('too big')
print (result)

result = old<num
print ('too small')
print (result)

result = old==num
print ('oh,yes!')
print (result)
