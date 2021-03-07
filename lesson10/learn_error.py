# 其他语言 Exception 异常
# Python 叫 Error 异常、错误



# if b == 0:
#     print("不能除以0")
# else:
#     print(f'{a} / {b} = {a / b}')

def if_func(c):
    if c:
        return

    print("haha")

def y():
    a = int(input('请输入被除数: '))
    b = int(input('请输入除数: '))

    try: # 代码是一句句往下执行的
        print(f'{a} / {b} = {a / b}')
        with open('lesson10/learn_write.txt',"r+") as f:
            f.write('hahahahahafdsafdsafdsa\n')
            # f.read()
        return #返回
    except ZeroDivisionError:
        print("发生了除以0的错误")
    except FileNotFoundError:
        print("发生了找不到文件的错误")
    except:
        #print("发生了其他的错误")
        pass
    else: # try里的代码没有发生错误 或者 except里的代码没有被执行 (并且没有提前返回)
        print("没有发生错误")

print("再见")

x = y() # x == None