import re

# # 1.匹配某个字符串
# text= 'hello,h1,hehehheheheheeeeee'
# ret = re.match('he',text)
# print(ret.group())



# 2.点：匹配任意字符(不能匹配换行符)
# text= '+ahello,h1,hehehheheheheeeeee'
# ret = re.match('.',text)
# print(ret.group())


# 3.\d:匹配任意的数字（0-9）

# text ="3124512341243"
# ret =re.match('\d',text)
# print(ret.group())


# 4.\D:匹配任意的非数字

# text ="sdas124das51asd2341243"
# ret =re.match('\D',text)
# print(ret.group())

# 5. \s；匹配空白字符(\n,\t,\r,空格)
# text ="\rdas51asd2341243"
# ret =re.match('\s',text)
# print(ret.group())

# 6.\w：匹配a-z和A-Z以及数字
#
# text ="11Asd\rdas51asd2341243"
# ret =re.match('\w',text)
# print(ret.group())

# 7.\W:与\w相反
# text =" +11Asd\rdas51asd2341243"
# ret =re.match('\W',text)
# print(ret.group())


#[]组合的方式，只要满足中括号中的字符就可以匹配

# text ="0731-7887123asdasdasd"
# ret =re.match('[\d\-]+',text)
# print(ret.group())
# output:0731-7887123


# 中括号的形式代替\d:[0-9]
# text ='a09'
# ret = re.match('[0-9]',text)
# print(ret.group())
#
# # 中括号的形式代替\D:[^0-9]
# text ='a09'
# ret = re.match('[^0-9]',text)
# print(ret.group())

# # # 中括号的形式代替\w:[a-zA-Z0-9]
# text ='a09'
# ret = re.match('[a-zA-Z0-9]',text)
# print(ret.group())


# # # 中括号的形式代替\W:[^a-zA-Z0-9]
# text ='$%#$#&^%$&^5675a09'
# ret = re.match('[^a-zA-Z0-9]',text)
# print(ret.group())


#匹配多个字符
#1.*：匹配0个或多个字符
# text ='567511a0aaaa1111119'
# ret = re.match('\d*',text)
# print(ret.group())
#
#
# #2.+:匹配1个或多个###   >=1
# # 多个字符>=1
# text ='abcd'
# ret = re.match('\w+',text)
# print(ret.group())


##3.?:匹配1个或0个
# text =' 1abcd'
# ret = re.match('\w?',text)
# print(ret.group())

# 4.{m}匹配m个字符：
# text ='1abcd'
# ret = re.match('\w{3}',text)
# print(ret.group())
# # 5.{m,n}匹配m-n个字符：
# text ='1a+bcd'
# ret = re.match('\w{1,4}',text)
# print(ret.group())


############小案例############
# 验证手机号码：
# text ='15958036201'
# ret = re.match('1[34568]\d{9}',text)
# print(ret.group())

# 验证邮箱：
# text ='hzj.boxes@gmail.com'
# ret = re.match('.+@[a-z0-9]+\.[a-z]+',text)# . 加反斜杠之后反义无正则表达式中的.的意思
# print(ret.group())

# 验证url:
# text ='https://www.gushiwen.org/default_2.aspx'
# ret = re.match('(http|https|ftp)://[^\s]+',text)# . 加反斜杠之后反义无正则表达式中的.的意思
# print(ret.group())

# 验证身份证：
# text ="330282199708145531"
# ret = re.match('\d{17}[Xx\d]',text)# . 加反斜杠之后反义无正则表达式中的.的意思
# print(ret.group())

# ^(脱字号)
# text ="hello"
# ret = re.search('^h',text)# 以。开始
# print(ret.group())


#  $:以...结尾：
# text ="hello@163.com"
# ret = re.match('.+@163.com$',text)# 以。开始
# print(ret.group())


# |:匹配多个字符串或表达式
# text ='https://www.gushiwen.org/default_2.aspx'
# ret = re.match('(http|https|ftp)://[^\s]+',text)# . 加反斜杠之后反义无正则表达式中的.的意思
# print(ret.group())

# 贪婪模式和非贪婪模式
# text ='0123456'
# ret = re.match('\d+?',text)# . 加反斜杠之后反义无正则表达式中的.的意思
# print(ret.group())
#非贪婪模式 ? 满足的最小条件
# text ='<h1>zxc</h1>'
# ret = re.match('<.+?>',text)# . 加反斜杠之后反义无正则表达式中的.的意思
# print(ret.group())

##############匹配0-100的数字不包括09,101,1001
text ='100'
ret = re.match('[1-9][0-9]?$|100$',text)# . 加反斜杠之后反义无正则表达式中的.的意思
print(ret.group())
