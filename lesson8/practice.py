# def display_message():
#     print("本章学习了定义函数")
# for i in range(10):
#     display_message()
# def favourite_book(title):
#     print(f"One of my favorite books is {title}.")
# favourite_book("Alice in Wonderlan")

# def make_shirt(a = 'T', b = 'I love Python'):
#     return f"订购的shirt的尺码为{a}\n打印的内容为{b}"

# print(make_shirt())

# 8-6
# def city_country(city, country):
#     a = f"{city}, {country}"
#     return a.title()

# print(city_country("santiago", "chile"))

# 8-7
# def make_album(singer, album, count=None):
#     if count != None:
#         a = {"name": singer, "album": album, "count": count}
#     else:
#         a = {"name": singer, "album": album}
#     return a

# print(make_album("d", "song1", 4))
# print(make_album("b", "song2"))
# print(make_album("c", "song3"))

# def make_album(singer, album, count=None):
#     if count != None:
#         a = {"name": singer, "album": album, "count": count}
#         return a
#     a = {"name": singer, "album": album}
#     return a

# 8-8

def make_album(singer, album, count=None):
    a = {"name": singer, "album": album}
    if count:
        a["count"] = count
    return a

while True:
    b = input("请输入singer: ")
    if b == "quit":
        break
    c = input("请输入专辑的名称：")
    if c == "quit":
        break
    print(make_album(b, c))

