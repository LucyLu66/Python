import re
text = "Hi, I am Shirley Hilton. I am his wife."

#“.”在正则表达式中表示除换行符以外的任意字符。
m = re.findall(r".", text)

#“\S”，它表示的是不是空白符的任意字符
m = re.findall(r"\S", text)

#“*”表示数量,会匹配尽可能长的结果
m = re.findall(r"I.*e", text)

#匹配到最短的就停止，需要用“.*?”。
m = re.findall(r"I.*?e", text)

m = re.findall(r".*", text)

if m:
    print(m)
else:
    print('not match')

#WORK
#从下面一段文本中，匹配出所有s开头，e结尾的单词。
test ="site sea sue sweet see case sse ssee loses"
out = re.findall(r"\bs\S*e\b", test)
if out:
    print(out)
else:
    print('not match')

