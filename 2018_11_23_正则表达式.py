import re   #re是python里的正则表达式模块
text = "Hi, I am Shirley Hilton. I am his wife."
m = re.findall(r"hi", text)    #字符串前面加了r，是raw的意思，它表示对字符串不进行转义。
#findall是其中一个方法。返回结果是一个包含所有匹配的list。

#使用“\bhi\b”这个正则表达式,“\b”在正则表达式中表示单词的开头或结尾，空格、标点、换行都算是单词的分割。
m = re.findall(r"\bHi\b", text)

#[]表示满足括号中任一字符
m = re.findall(r"[hi]", text)

#如果把正则表达式改为“[Hh]i”，就可以既匹配“Hi”，又匹配“hi”了。
m = re.findall(r"[Hh]i", text)
if m:
    print(m)
else:
    print('not match')

