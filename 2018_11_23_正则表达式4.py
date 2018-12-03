#写一个正则表达式，能匹配出以下多种格式的电话号码
import re
phone = "(021)88776543 010-55667890 02584453362 0571 66345673"

num = re.findall(r"\(?0\d{2,3}[) -]?\d{7,8}", phone)

if num:
    print(num)
else:
    print('not match')
