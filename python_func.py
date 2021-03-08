# python 内建函数
'''
# 1) 使用import将库函数导入进来
#  1) import lib
import random #库
for i in range(5):
    print(random.randint(1, 10))  #[1~10]  randint是random库的函数
'''
'''
#  2) from lib import fnc 用法
from random import randint #库及函数名
for i in range(5):
    print(randint(1, 10))  #[1~10]  randint是random库的函数
'''
#  3) from lib import* 用法
from random import * #库及 所有 函数
for i in range(5):
    print(randint(1, 10))  #[1~10]  randint是random库的函数