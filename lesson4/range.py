# for value in range(1,5):
#     print(value)
# numbers=list(range(1,5,2))
# print(numbers)

# squares=[]
# for value in range(1,11):
#     square=value**2
#     squares.append(square)
# print(squares)

# digits=[1,2,3,4,5,6,7,8,9,0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))
# a=len(digits)
# print(a)

# def avg(a):
#     return sum(a) / len(a)

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(avg(digits))



# def multiply(a, b):
#     m=a*b
#     return m

# m = multiply(2, 4)
# print(m)

# # 列表 -公式-> 另外一个列表

# a = [1, 2, 3, 4]
# b = [x+3 for x in a]
# # y = f(x) = x + 3
# print(b)

# 4.4.1 切片

# a = [3, 6, 8, 1, 7, 2]

# b = a[:] # [2,5)
# # [8, 1, 7]

# print(b)

# 思考快与慢（从第44页到第135页）

# a = [3, 6, 8, 1, 7, 2]
# b = a[:]

# print(a)
# print(b)

# a[1]=5
# print(a)
# print(b)

# b[2]=9
# print(a)
# print(b)


# 4.5 元组

# 列表是可变的
# a = [3, 6, 8, 1, 7, 2, 9]
# #del a[2]
# print(a)

# 元组是不可变的 tuple
a = (3, 6, 8, 1, 7, 2, 9)
# a[0] = 12
# del a[1]
for i in a:
    print(i)

a = 12

a = 12
a = [121, 131]
del a[0]
print(a)

# genders = ('男', '女', '其他')
# genders.append(12)

excel1 
excel2

a = [1, 2, 3, 4, 5]
b = [3, 4, 5]

for i in b:
    a.remove(i)

