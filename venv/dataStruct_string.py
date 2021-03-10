# 字符串
# 多行'''
print('''
hello bob,
test
yours,
''')

# 多行注释
'''
注释1
注释2
注释3
'''
#字符串像列表一样，使用下标和切片。
spam = 'Hello world!'
print(spam[1])
print(spam[1:4])

#转换大小写 字符串方法upper()、lower()、isupper()和islower()
'''
isalpha()返回True，如果字符串只包含字母，并且非空；
isalnum()返回True，如果字符串只包含字母和数字，并且非空；
isdecimal()返回True，如果字符串只包含数字字符，并且非空；
isspace()返回True，如果字符串只包含空格、制表符和换行，并且非空；
.istitle()返回True，如果字符串仅包含以大写字母开头、后面都是小写字母的单词。
'''
s1 = 'This Is Title Case 123'.istitle()
s2 = 'This Is not Title Case'.istitle()
print(s1,s2)

import math
print ( math.sin(1.57) )