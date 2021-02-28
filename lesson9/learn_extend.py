# class Car:
#     def __init__(self):
#         self.odometer_reading = 0

#     def get_odometer(self):
#         """getter"""
#         return self.odometer_reading

#     def set_odometer(self, o):
#         """setter"""
#         self.odometer_reading = o

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles


# # 值可以被返回，类的属性是值，所以类的属性可以被返回

# car = Car()

# # 下面三段，每段的每行等价

# car.odometer_reading = 12
# car.set_odometer(12)

# print(car.get_odometer())
# print(car.odometer_reading)

# car.odometer_reading += 10
# car.increment_odometer(10)
# car.set_odometer(car.get_odometer() + 10)
# car.odometer_reading = car.get_odometer() + 10


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"用户的名字是{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"{self.first_name} {self.last_name}:祝福快快乐乐每一天！")

# user1 = User("Albert", "Johnson")
# user2 = User("Yoyo", "Johnson")
# user1.describe_user()
# user2.greet_user()

# 继承
# VipUser类继承了User类
# VipUser是User的子类
# User是VipUser的父类
class VipUser(User):

    def __init__(self, first_name, last_name, money):
        super().__init__(first_name, last_name)
        self.money = money

    def describe_user(self):
        super().describe_user()
        print(f"VIP余额为 {self.money}")

# vip_user = VipUser('Yoyo', 'Hahah', 520)
# vip_user.describe_user()

class SuperVipUser(VipUser):

    def __init__(self, first_name, last_name, money, score):
        super().__init__(first_name, last_name, money)
        self.score = score

    def describe_user(self):
        super().describe_user()
        print(f"SUPERVIP积分为 {self.score}")

    def set_score(self, score):
        self.score = score

    def get_money(self):
        return self.money

vip_user = SuperVipUser('Yoyo', 'Hahah', 520, 100000)
vip_user.describe_user()

