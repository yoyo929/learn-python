# 列表(list, 数组)

# a = [3, 543, 3] # 整型列表
# hello = "bye"
# b = [hello, 'yoyo', 'world'] # 字符串列表
# b = ['bye', 'yoyo', 'world'] # 字符串列表
# c = [1.2, 0.5, 100.6] # 浮点数列表
# c = ["1.2", "0.5", "100.6"] # 浮点数列表

# 'y' 字符
# 'bye' 字符串

# a = [2, 0, 3, 3]
# print(a) # [12, 2, 0, 3, 3] 
# a.insert(0, 12)
# print(a) # [12, 2, 0, 3, 3]
# a.insert(-1, 1)
# print(a) # [12, 2, 0, 3, 1, 3]
# del a[0] # del is short for delete
# print(a)
# del a[-1] # del is short for delete
# print(a)
# b = a.pop(
# 1) # pop 弹出
# print(f'a: {a}, b: {b}')

# a = [3, 0, 2, 3]
# # del a[1] 按索引删除
# a.remove(3) # 按值删除
# print(a)

# 3.3.1 - 3.3.2
# a = [432, 5, 54, 77, 32, 3, 4]
# print(a)
# a.sort(reverse = True)
# print(a)

# a = [432, 5, 54, 77, 32, 3, 4]

# b = a.copy()
# b.sort()

# print(a)
# print(b)

# a = [432, 5, 54, 77, 32, 3, 4]

# b = sorted(a)

# print(a)
# print(b)

# 3.3.3
# a = [432, 5, 54, 77, 32, 3, 4]

# a.reverse()
# print(a)

# a.reverse()
# print(a)

# 3.3.4
# a = [432, 5, 54, 77, 32, 3, 4]
# l = len(a) # length 长度
# print(l)

# 交互模式，命令行直接执行 python

# 3.4 避免索引错误

# blablah 100 这些会正常执行
a = [432, 5, 54, 77, 32, 3, 4] # 长度为 7 , index ∈ [-7, 7)
# 长度为n，索引的范围就是左闭右开的-n到n

index = -9
length = len(a)

if index < -7 or index >= 7: # 为了避免异常，可以自己做检查
  print(f'你这个索引好像不太对, 因该是-7到7， 而你的索引是 {index}')
  exit()

b = a[index] # 程序会在异常处退出
# blablah 100 再也不会执行了

# 异常
# IndexError: list index out of range
# 索引错误：列表的索引超出范围

# 可复用性
# 写死