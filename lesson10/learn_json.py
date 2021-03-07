# JSON is short for JavaScript Object Notation
# 是一种数据存储格式，就像python里的字典

# JSON Object <-- {} --> Python的dict 对象，字典
# JSON Array <-- [] --> Python的list 数组，列表

# module 是模块的意思
import json

# numbers = [2, 3, 5, 7, 11, 13]

# with open('lesson10/numbers.json', 'w') as f:
#     json.dump(numbers, f) # 把numbers转换为json格式，写到f里

# # JSON里面的字符串必须用双引号，布尔值全小写 true/false
# yoyo = {'name': 'yoyo', 'gender': 'female', 'birthday': '1990-09-29', 'hobbies': ['read', 'yoga', 'run'], 'love_gt': True}

# with open('lesson10/yoyo.json', 'w') as f:
#     json.dump(yoyo, f) # 把yoyo转换为json格式，写到f里


# with open('lesson10/numbers.json') as f:
#     numbers = json.load(f)
#     print(numbers)

# with open('lesson10/yoyo.json') as f:
#     yoyo = json.load(f)
#     print(yoyo)

def write_json_to_file(obj, path):
    with open(path, 'w') as f:
        json.dump(obj, f)

with open('lesson10/users.json', 'r') as f:
    users = json.load(f)

operation = input('请输入你的操作，1表示登录，2表示注销，3表示查看状态: ')
username = input('请输入你的名字: ')
if operation == '1':
    if username in users:
        print(f'你好，{username}，你已经登录过了')
    else:
        print(f'你好，{username}，你成功登录了')
        users.append(username)
        # with open('lesson10/users.json', 'w') as f:
        #     json.dump(users, f)
        write_json_to_file(users, 'lesson10/users.json')
elif operation == '2':
    if username in users:
        print(f'再见，{username}')
        users.remove(username)
        # with open('lesson10/users.json', 'w') as f:
        #     json.dump(users, f)
        write_json_to_file(users, 'lesson10/users.json')
    else:
        print('你没登录过，先登录再说')
elif operation == '3':
    if username in users:
        print(f'{username} 已登录')
    else:
        print(f'{username} 未登录')
else:
    print('你输入的操作不正确')
