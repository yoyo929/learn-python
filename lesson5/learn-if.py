# 自己给文件/变量起名尽量避开python的关键字和常用函数

cars = ['audi', 'bmw', 'subaru', 'toyota']

# a = True

# for car in cars:
#     if a:
#         print(car.upper())
#         a = False
#     else:
#         print(car.title())
#         a = True

# 5.2
# == 判断两边是否相等，如果相等，则值为True，否则为False
# = 赋值号，计算赋值号右边的值赋值给左边

# a = 2 == 1

# 遍历
# cars = ['audi', 'BmW', 'subaru', 'toyota']

# for car in cars:
#     if car.upper() != 'BMW':
#         print(car.upper())
#     else:
#         print(car.title())

# 大小写是否敏感 case insensitive(不敏感)

# age = 1 # 定义+赋值
# age = 18 # 赋值/修改
# age == 18

# age = 17

# if age >= 18:
#     print('这是一个成年人')
# else:
#     print('未成年')

# score = 70

# # [0, 60) ∪ [90, 100]
# # if score < 60 or score >= 90 or score == 70:
# #     print('需要谈话')
# # else:
# #     print('不需要谈话')

# a = score >= 65 and score < 70

# if a: #[65, 70) Z
#     print('继续努力')
# else:
#     print('随便')

cars = ['audi', 'bmw', 'subaru', 'toyota']

a = 'xiaopeng' not in cars

if a:
    print('我没有xiaopeng')
if b:
    print()
if c:
    print()
else: 
    print()

requested_toppings = []

if requested_toppings:
    print()

