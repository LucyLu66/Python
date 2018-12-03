a = 2
while a!=0:
    print ('please input')
    a = int(input())
print ('over!')

print('---------------------------------')

num = 10
print ('Guess how old am I?')
answer = False

while answer==False:
    old = int(input())
    if old<num:
        print ('small')
    if old>num:
        print ('big')
    if old==num:
        answer=True
        print ('yes!')

