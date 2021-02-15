# a = [1, 2, 3, 4, 5]

# a[5] = 100

# # list []
# # tuple ()
# # dict {}

# a = ['hello', 12, [1, 2, 3, 4], {'a':'b'}]

# yoyo = { 'name': 'You Yuxin', 'age': 30, 'gender': 'female', 'birthday': 'hahaha' }

# a = {'key1': 'Hello', 'key2': 12, 'key3': [1, 2, 3, 4], 'key4': { 'a': 'b' }, 'key5': True}

# # 键 key
# # 值 value
# # 键值对 pair

# print(yoyo)

# print(yoyo['age'])

# yoyo['birthday'] = '1990-09-29'

# print(yoyo)

# del yoyo['birthday']

# print(yoyo)

# d = {}

# d['color'] = 'green'
# d['points'] = 5

# print(d)

# d['points'] -= 12

# print(d)

# x_positions = 12
# y_positions = 3
# speed = 'slow'

# alien = { 'has_a_house': True, 'x': 0, 'y': 3, 'speed': 'slow' }

# x = alien.get('z')

# if x == None:
#     print('字典中没有z')
# else:
#     print(f'字典中有z: {x}')

# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }

# # for name, language in favourite_languages.items():
# #     print(f"{name.title()}'s favorite language is {language.title()}")

# if f(6) == 9:
#     print('ok')

# for key in sorted(favourite_languages.keys()):
#     print(key)


aliens = []

for i in range(30):
    b = {'color': 'green', 'points': i, 'speed': 'slow'}
    aliens.append(b)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)

print('...')

# print(aliens)

# values = []

# for i in range(10):
#     a = i * i
#     b = a + 1
#     values.append(b)

# print(values)

# haha = []

# for i in range(5):
#     b = [1, 2, 3]
#     haha.append(b)

# print(haha)

