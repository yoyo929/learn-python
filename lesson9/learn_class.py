class Dog: # 表示一类事物的名词，首字母大写
    """狗"""

    def __init__(self, name, age): # 构造函数/方法；intialize 初始化，init
        """初始化属性 name 和 age"""
        self.name = name
        self.age = age

    def sit(self): # 类的方法 method
        print(f"{self.name} 坐下")

    def roll_over(self): # 类的方法
        print(f"{self.name} 打滚")

# 类的实例/对象 object
# 实例化一条狗/构造一条狗/创建一条狗
# a = Dog('伊巴', 3) # 用类名加上__init__函数除了self之外的参数进行构造
# a.sit() # 调用类的方法时，使用 object.method(arguments) 的格式进行调用，
# # arguments 是除了 self 之外的参数
# a.roll_over()

# b = Dog('乐乐', 5)
# b.sit()
# b.roll_over()

class Person:
    def __init__(self, name, gender, age): 
        self.name = name
        self.gender = gender
        self.age = age

    def self_introduct(self):
        print(f"Hi, I'm {self.name}. I'm {self.age} years old.")

    def love(self, another_person):
        print(f"{self.name} love {another_person.name}")

    def can_drink(self):
        return self.age >= 18

    def drink(self, wine):
        print(f"{self.name} 喝了一口 {wine}")
    
    def happy_birthday(self): # 类的方法
        self.age += 1

gege = Person('Albert', '男', 30)
gege.self_introduct()
gege.name = 'Tony'
gege.age = 12
gege.self_introduct()
gege.happy_birthday()
gege.self_introduct()

# yoyo = Person('YoYo', '女', 30)
# yoyo.self_introduct()

# if gege.can_drink():
#     gege.drink('茅台')
# else:
#     print(f"{gege.name} 不能喝酒")

# gege.love(yoyo)
# yoyo.love(gege)

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, to_add):
        self.number_served += to_add

    def get_number_served(self):
        return self.number_served

    def add_cuisine_type(self, new_cuisine_type):
        self.cuisine_type += ','
        self.cuisine_type += new_cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} 是一家 {self.cuisine_type} 的餐厅。")

    def open_restaurant(self): 
        print(f"{self.restaurant_name}正在营业。")

    

zhijiang = Restaurant("zhijiang", "japanese food")
print(zhijiang.number_served)
zhijiang.number_served = 121
print(zhijiang.number_served)
zhijiang.set_number_served(130)
print(zhijiang.number_served)
zhijiang.increment_number_served(4)
print(zhijiang.number_served)
# print(zhijiang.restaurant_name) #self = 实例(打印两个属性)
# print(zhijiang.cuisine_type)
# zhijiang.describe_restaurant()#调用前述的两个方法 BBQ
# zhijiang.open_restaurant()

# haidilao = Restaurant("haidilao", "hot pot")
# haidilao.describe_restaurant()
# qingjiaoyu = Restaurant("qingjiaoyu", "fish")
# qingjiaoyu.describe_restaurant()
# henjiuyiqian = Restaurant("henjiuyiqian", "barbecue")
# henjiuyiqian.describe_restaurant()

# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def describe_user(self):
#         print(f"用户的名字是{self.first_name} {self.last_name}")

#     def greet_user(self):
#         print(f"{self.first_name} {self.last_name}:祝福快快乐乐每一天！")

# user = User("Albert", "Johnson")
# user.describe_user()
# user.greet_user()

# # user是一个对象 object





           


