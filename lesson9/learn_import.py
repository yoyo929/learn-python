#from learn_extend import User, VipUser, SuperVipUser

# Python 标准库 standard libraries

from random import randint

b = [randint(0, 4) for i in range(20)]
print(b)

from datetime import datetime

now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))