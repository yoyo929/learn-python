# path = 'D:/PythonWorkspace/learn-python/lesson10/pi_digits.txt'

# 土鳖写法
# f = open(path)
# contents = f.read()
# print(contents)
# f.close()

# with open('pi_digits.txt') as f: # 一个点表示当前目录，两个点表示上一级目录
#     contents = f.read() # 把整个文件读出来
#     print(contents)

# with open('pi_digits.txt') as f: # 
#     for line in f: # 把所有行一行一行读
#         print(line.rstrip())

# 要合并结果，通常都是先定义一个变量（选择合适的初始值），
# 然后遍历要合并的序列/列表，把每个元素合并到那个变量上

# a = [1, 2, 3, 4, 5]
# s = 0
# for i in a:
#     s += i
# print(s)

# b = 1
# for i in a:
#     b *= i
# print(b)

# '' 空字符串、空串
# ' ' 一个空格
# None 空、没有

# with open('pi_digits.txt') as f: # 一个点表示当前目录，两个点表示上一级目录
#     lines = f.readlines() # 读成列表
    
#     pi_string = ''
#     for line in lines:
#         pi_string += line.rstrip()

#     print(pi_string)
#     print(lines)

# with open('lesson10/pi_digits_million.txt') as f: # 可读
#     pi = f.read()

#     while True:
#         birthday = input('请输入你的生日：')

#         if birthday == 'q':
#             break

#         if birthday in pi:
#             print("你的生日出现在圆周率前100万位中")
#         else:
#             print("你的生日没有出现在圆周率前100万位中")

# Ctrl + C 
# 退出程序

# 171

# with open('lesson10/learn_write.txt', 'a') as f:
#     f.write('hahahahahafdsafdsafdsa\n')
#     f.write('jfdkslajkdlsjfkladsjfkl\n')
#     f.write('rewrewteryrteuytrurtu\n')

# 178
# 10.3.6 分析文本
# int is short for integer # int 是 integer 的缩写，integer 是整数的意思
# str is short for string

# sentence = "I.Love.You"
# words = sentence.split('.') # 没有给出参数时，默认为用空格分隔
# print(words)

# 布尔
# 整数
# 浮点数
# 字符串

# with open('lesson10/learn_write.txt') as o:
#     s = o.read()
#     words = s.split()
#     print(f'这个文件里有 {len(words)} 个单词')
#     print(f'文件里总共有 {len(s)} 个字符')
#     print(words)


# 封装
def count_words(path):
    with open(path) as o:
        s = o.read()
        words = s.split() # split 默认用所有空白字符分割 \n \t 空格
        return len(words)

# wc = count_words('lesson10/learn_write.txt')
# print(wc)

file_list = ['lesson10/learn_write.txt', 'lesson10/pi_digits.txt']
for f in file_list:
    print(f'{f} 文件的单词个数为: {count_words(f)}')

def do_nothing():
    pass

