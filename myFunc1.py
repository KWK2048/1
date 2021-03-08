# define a new func

def hello():  # 注意冒号
    print('hello!')
    print('hello!!')
    print('hello!!!')
hello()

def Hi(name):  # 传参
    print('Hi ' + name)
Hi('David')

# 返回值return
def Stu_grade(level):
    if level=='A':
        print("You got 90-100 points")
        return 1
    elif level == 'B':
        print("You got 80-90 points")
        return 2
    else:
        print("You got <80 points")
        return 3

# Stu_grade('A')  # 如何不用引号转化为str？
print("返回值是", Stu_grade('A'))


print('car','truck','pedestrain','bicycle', sep=',') # 注意sep的用法
print('car','truck','pedestrain','bicycle', sep=',,,') # 注意sep的用法


#定义全局变量
myNum=100
def getNum():
    print('全局变量myNum=', myNum)
    return 0
getNum()

# 如果在函数内定义全局变量，需要用global
def test1():
    global egg
    egg = '全局变量'
test1()  #要先运行该函数，才能声明这个变量
print(egg)
######################### 定义函数时，不鼓励使用全局变量

# 错误可以由try和except语句来处理。那些可能出错的语句被放在try子句中。如果错误发生，程序执行就转到接下来的except子句开始处。
def test2(num1):
    try:
        return 42/ num1
    except ZeroDivisionError:
        print('错误，除数不能是0')
        return 555
print( test2(3) )
print( test2(0) )
