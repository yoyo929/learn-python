# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
# age = input('How old are you?\n')
# age = int(age)

# # age = int(input('How old are you'))

# if age >= 18:
#     print('You are an adult.')
# else:
#     print('You are a child.')

# 7.1.3 求模
# ball_num 个球， 还有一些框子，每个框子能装 ball_per_box 个球，
# 总共需要多少个框子来装 ball_num 个球

# ball_num = 17
# ball_per_box = 5

# remainder = ball_num % ball_per_box
# box_num = ball_num // ball_per_box

# if remainder > 0:
#     box_num += 1

# print(box_num)

# 7.2  while 循环

# 死循环
# a = [1, 2, 3, 4, 5, 6, 7]

# while a:
# # #     for i in range(len(a)):
# # #         a[i] += 1
#     print(a)
#     a.pop()

# 字典也可以用len来求键值对的个数
# a = { 'ha':1, 'ok':'12' }
# print(len(a))

# for i in range(1, 6):
#     print(i)

# Ctrl + C

# prompt = "fdsafdsafdsafsda"
# message = ""

# while message != 'quit':
#     message = input(prompt)
#     print(message)


# 关键字
# 循环
# 条件

# break

# prompt = "Please enter quit to end the program: "

# while True:
#     message = input(prompt)

#     if message == 'quit':
#         break # 退出循环

#     if message == 'aaa':
#         continue

#     print(message)


# 不能同时按索引遍历和删除同一个列表
pets = ['cat', 'cat', 'cat', 'cat', 'cat']

# 错误1
# for i in pets:
#     if i == 'cat':
#         pets.remove(i)

# 错误2
# index = 0
# while index < len(pets):
#     if pets[index] == 'cat':
#         pets.remove('cat')
#     index += 1

# 正确
# 

# print(pets)

responses = {}
name = 'yoyo'

responses[name] = 1
responses['name'] = 2

print(responses)
