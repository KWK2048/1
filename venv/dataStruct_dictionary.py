# 字典，用{}，没有顺序的概念，
# 列表适用于包含一组有序的值，字典适合于包含关联的键与值。
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# key(), value(), items()
print('keys = ', birthdays.keys())
print(birthdays.values())
print(birthdays.items())
# [] 通过关键字，获取对应值
print(birthdays['Alice'])
# print(birthdays['kwk'])  # 不存在 报错

# get()
print(birthdays.get('Bob',0))
print(birthdays.get('Bob2',0))   #返回0

# 如果该键不存在时要设置xin值。如果该键确实存在，方法就会返回键的值。
birthdays.setdefault('kwk', 'feb 15')
birthdays.setdefault('kwk', 'feb 25')
print(birthdays.values())

# 例子
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)   # 发现新字母，则置零； 已有字母，返回关键字的对应值
    count[character] = count[character] + 1    # 数字+1

print(count)
#

'''while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
'''
