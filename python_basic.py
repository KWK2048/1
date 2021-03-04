# 2021.3
# to fast practise the PYTHON skills, mainly focus on diff between Cpp and python.
print('hello, world')
# 顺序结构、选择结构、循环结构
print('-----顺序结构------')
print(1)
print(2)
print(3)
print('-----选择结构------')
'''
money = 1000  # 余额
s = int(input('请输入取款金额'))
# 判断余额是否充足
if money >= s:
    money = money-s
    print('取款成功，余额为', money)
'''

'''
# 判断输入的是奇数还是偶数
num = int(input('please input a int number'))
if num%2 == 0:
    print('偶数')
else:
    print('奇数')
'''
'''
# 录入一个成绩，90-100 A; 80-90 B; 70-80 C; 70-0 D; >100 OR <0 非法数据
gradeNum = int(input('please input a score of the student'))
if 90 <= gradeNum <= 100:
    print('A')
elif gradeNum >= 80 and gradeNum < 90:
    print('B')
elif gradeNum >= 70 and gradeNum < 80:
    print('C')
elif gradeNum >= 0 and gradeNum < 70:
    print('D')
else:
    print('invalid input')
'''
'''
print('------------嵌套if语句----------')
# 会员卡购物，大于200时8折；大于100时9折；非会员不打折
clubmember = int(input('Are you clubmember, yes-1; no-0 \n'))
if clubmember == 1:
    fee = float(input('how much is your fee? \n'))
    if 100 <= fee < 200:
        fee = fee *0.9
    elif fee >= 200:
        fee = fee*0.8
    print('dear clubmember\n, you need to pay',fee,'  with discount')

elif clubmember == 0:
    pass  # pass 没有实际意义，用于搭建架构时占位符，用于以后放语句的地方
    print('please checkout without discount')
'''
# range()
r1 = list(range(10))
r2 = list(range(1, 10))
r3 = list(range(1, 10, 3))
print(r1, r2, r3)
