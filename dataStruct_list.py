# List
# 列表 即 数组？
'''
myList1 = ['car', 'dog', 'tiger', 'butterfly']
print (myList1[1])
print (myList1[-3])  # 负下标
print (myList1[1:3])    # 3不包括,相当于[1,3)
print (myList1[:])  # 所有

del myList1[1]  # 删除一个元素
print (myList1[:])  # 所有
'''
'''
# 举例，用一个列表保存 相似数据
catNames = []
while True:     #循环好方法
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break    #结束循环
    catNames = catNames + [name] # list concatenation #增加数组元素的方式
print('The cat names are:')
for nam in catNames:    #随意定义参数，是指等于list的元素，打印，并循环
    print(' ' + nam)

# print(catNames)
# print(nam)
'''

# index(), append(), insert(), remove(),sort(), sort( reverse=ture ) 以上是list常用方法

# 列表是“可变的”数据类型，它的值可以添加、删除或改变。
# 但是，字符串是“不可变的”，它不能被更改。


# 除了两个方面，“元组”数据类型几乎与列表数据类型一样。
# 首先，元组输入时用圆括号()，而不是用方括号[]。
# 区别还在于，元组像字符串一样，是不可变的。元组不能让它们的值被修改、添加或删除。

# 如果需要元组值的一个可变版本，将元组转换成列表就很方便。
mylist1=list(('cat', 'dog', 'tiger'))
# print (mylist1[1])
for i in range(len(mylist1)):
    print(mylist1[i])

# 列表的数据赋值给新参数，是引用方式 ！！！！！！！
mylist2 = mylist1
mylist1[0] = 'padan'
for i in range(len(mylist1)):
    print(mylist1[i])

# list传参，可以直接改变值 ！！！！ 如果不想改变其值，需要用copy模块
def eggs(somePar):
    somePar.append('Hello')
spam = [1, 2, 3]
eggs(spam)
print(spam)

# 对比copy的作用
def eggs(somePar):
    somePar.append('Hello')
spam1 = [1, 2, 3]
spam2 = spam1
eggs(spam2)
print(spam1,spam2)

import copy
def eggs(somePar):
    somePar.append('Hello')
spam3 = [1, 2, 3]
spam4 = copy.copy(spam3)
eggs(spam4)
print(spam3,spam4)
