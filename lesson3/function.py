# 函数
# 内建 约等于 自带 内置print

# f() 
# f(n) 
# y=f(x) 

# 使用函数、调用函数时使用的参数叫 实参
# 定义函数的时候的参数叫 形参

# def print_n_star(n):
#     print("*" * n)

# for i in range(1, 10):
#     print_n_star(i)

# ###########################

# def print_six_star():
#     print("*" * 6)

# for i in range(1, 10):
#     print_six_star()

###########################

# 求正方形的面积
def area_of_square(x):
    #return x * x
    return area_of_rectangle(x, x)

# 求平方和 y = a^2 + b^2
def sum_of_squares(a, b):
    return a * a + b * b

# 求长方形的面积
def area_of_rectangle(i, j):
    return i * j

a = sum_of_squares(3, 4)
print(a)