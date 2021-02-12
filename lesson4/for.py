# majicians=['alice','david','carolina']
# for majician in majicians:
#     print(F"{majician.title()},that was a great trick!")
#     print(f"I can't wait to see your next trick,{majician.title()}.\n")

# majicians = ['alice', 'david', 'carolina']
# for majician in majicians:
#     print(f'{majician.title()}, that was a greate trick!')
#     print(f"I can't wait to see your next trick, {majician.title()}")
#     print()

# majicians = ['alice', 'david', 'carolina']
# for majician in majicians:
#     print(f'{majician.title()}, that was a greate trick!')
#     print()
#     print(f"I can't wait to see your next trick, {majician.title()}")

# 4.2.1
# for majician in majicians:
# print(majician)
# print()

# SyntaxError 语法错误
# IndentationError 缩进错误 1.少了缩进
# IndexError 索引越界/超出范围
# NameError 变量在使用之前没有定义（通常也可能是变量打错字了）
# TypeError 类型错误

#nami = 12 #定义一个整型变量叫name，并赋值为12
# name = 12
# print(name)

# 4.2.2
# 不太可能犯的错误，想清楚循环体内容就可以了

# 4.2.3
# name = 12
# print(name)

# 4.2.4
# 跟4.2.2相反，想清楚循环体内容就可以了

# 4.2.5
# for m in majicians # SyntaxError
#     print(m)

# / 斜杆，除法 2/3
# \ 反斜杠，通常用于转义 n

# 4.3.3
# min max sum
#print(max(majicians))

# 4.3.2
# r = range(0, 1_000_000, 1000)
# a_big_list = list(r)
# print(min(a_big_list))

# 4.3.4
# 用一个列表/范围构造一个新列表
# squares = []

# for i in range(1, 6):
#     squares.append(i ** 2)

# [1, 2, 3, 4, 5] -> [1, 4, 9, 16, 25]
# squares = [i ** 2 for i in range(1, 6)] # [1, 2, 3, 4, 5]

# print(squares)

a = ['a', 'b', 'c']
#b = ['aa', 'bb', 'cc']
b = [i*2 for i in a]
print(b)


print('\n'.join([''.join([('GTYYX/'[(x-y)%len('GTYYX/')]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))