# # def greet_user(n):
# #     """显示简单的问候语"""
# #     print("Hello!")
# #     for i in range(n):
# #         print(i)

# # greet_user(3)
# # greet_user(2)

# def greet_user(username):
#     """显示简单的问候语。"""
#     print(f"Hello, {username}!")

# def greet_and_say_goodbye(un):
#     greet_user(un)
#     print("bye!")

# def greet_and_say_goodbye_and_go_away(un):
#     greet_and_say_goodbye(un)
#     print('go away')

# greet_and_say_goodbye_and_go_away('yoyo')

# 可以使用原有的函数定义自己的函数
# 然后可以像调用系统函数那样调用自己定义的函数
# 可以嵌套多次
# 自定义的函数跟系统提供的函数的地位一样（比如print、range、max、len）

# f(x) = x + 3

# def f(x):
#     return x + 3

# y = f(6)
# print(y)

# 函数调用完成后会得到一个值，称作返回值，通常需要用一个变量接住这个值，
# 或者说将函数返回值赋值给一个变量
# 在函数定义的时候决定具体返回什么值，使用return关键字来返回

def get_formatted_name_0(first_name, last_name, middle_name = ""):
    if middle_name: # if len(middle_name) != 0:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

def get_formatted_name_1(first_name, last_name, middle_name = ""):
    if middle_name: # if len(middle_name) != 0:
        return f"{first_name} {middle_name} {last_name}".title()
    else:
        return f"{first_name} {last_name}".title()

def get_formatted_name_2(first_name, last_name, middle_name = ""): # 短路运算
    if middle_name: # if len(middle_name) != 0:
        return f"{first_name} {middle_name} {last_name}".title()
    
    return f"{first_name} {last_name}".title()

coder = get_formatted_name_0('john', 'hooker')
# print(coder)

# def func(): # 短路运算
#     if a:
#         return 0
    
#     if b:
#         return 1

#     if c:
#         return 2

#     return 3

# def func_():
#     if a:
#         return 0
#     elif b:
#         return 1
#     elif c:
#         return 2
#     else:
#         return 3



# def build_person(first_name, last_name):
#     person = {'first': first_name, 'last': last_name}
#     return person

# musician = build_person('yoyo', 'albert')
# print(musician)


# person = {}
# age = 12
# person['age'] = age
# # person['age'] = 'age'

# print(person)

# # {'age': 12}


# a = [1, 2, 3, 4]

# a[0] = 12

# b = 8
# a[1] = b

# None # 没有东西
# 0 # 有东西，这个东西是整数0
# "" # 有东西，这个东西是空的字符串

# a = "fdsafdsf"
# if a == "": # len(a) == 0
#     print('a是个空字符串')
# else:
#     print(f'a是{a}')


# 8.4

def print_list(l):
    for i in l:
        print(i)

cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     print(car)


def append_10_number(l):
    for i in range(10):
        l.append(i)

numbers = [9, 9, 9]
# print(numbers)
append_10_number(numbers)
append_10_number(numbers)
# print(numbers)
# for n in numbers:
#     print(n)

# print_list(cars)
# print_list(numbers)

def print_dict(d):
    for k, v in d.items():
        print(f"{k} => {v}")

d = {'a': 12, 'b': 13, 'c': 'jfdksajkld'}

# print_dict(d)

# 8.5

# 将任意多个位置实参收集为一个元组
def make_a_list(*elements):
    for e in elements:
        print(e)

# make_a_list('a', 'b')

# 类似于关键字实参

# 将任意多个关键字实参收集为一个字典
def build_profile(**user_info):
    print_dict(user_info)

# build_profile(a = 1, b = "fdsjkafjdsk", c = [1, 2, 3])
