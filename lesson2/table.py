a = input("请输入一个数:") # a "10000" + "2" = "100002"
n = int(a) # n 10000 + 2 = 10002

for i in range(1, n):
    for j in range(1, i+1):
        print(str(j) + "*" + str(i) + "=" + str(i * j), end = " ")
    print("")