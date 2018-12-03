import re
#抓取手机号
phone = "12546546645 lucy 15184424395, 27200320140, 18200320140 13688336942"
#表示数字的方法\d
#num = re.findall(r"\d", phone)

#表示任意长度的数字
num = re.findall(r"[0-9]*", phone)

#匹配出所有的数字串
num = re.findall(r"\d+", phone)

#要限定长度，就用{}代替+，大括号里写上你想要的长度。
num = re.findall(r"\d{11}", phone)

#想要再把第一位限定为1，就在前面加上1，后面去掉一位
num = re.findall(r"1[0-9]{10}", phone)

if num:
    print(num)
else:
    print('not match')