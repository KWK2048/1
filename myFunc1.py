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
