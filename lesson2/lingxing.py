
# 硬性规定：变量名命名 字母 下划线 数字(不能开头)
a = 1
a2 = 1
aaa222 = 2
a2b2c3 = 12
_a = 12
a_b2_ = 13

# 编码规范(非硬性规定)s

# number -> num
# index -> i
# count

# table_length = 13
# table_leg_length = 4


num = int(input("请输入最多*所在行数:"))
a = num
b = num
for i in range(1,num+1):
    print((a-1) *' ', (2*i-1)*'*')
    a -=1 #下三角
for j in range(1, num):
    print(j*' ', (2*b-3)*'*')
    b -=1

# this is a message