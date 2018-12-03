l = [365, 'everyday', 0.618, True]
l[-1] #表示最后一个元素
l[-3] #表示倒数第三个元素
l[1:3] #输出第一和第二个元素
l[:3] #不指定前面，就是从第一个开始
l[1:] #不指定后面，就是到最后一个结束
l[:] #都不指定，默认输出全部
l[1:-1]

##罚球小游戏
from random import choice

score_you = 0
score_com = 0

dir = ['left', 'center', 'right']

for i in range(5):
    print('=====Round %d - You kick! =====' %(i + 1))
    print('Choose one side to shoot:')
    print(list(dir))

    you = input() #输入射门方向
    print('You kicked ' + you)

    com = choice(dir) #电脑随机扑救方向
    print('Computer saved ' + com)

    if you != com: #方向不同，球进，玩家得分
        print('Goal!')
        score_you += 1
    else: #方向相同，电脑扑救成功，电脑得分
        print('Oops...')
        score_com += 1

    print('Your socre: ' + str(score_you))  #玩家得分
    print('Computer score: ' + str(score_com))  #电脑得分