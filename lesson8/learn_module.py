# 8.6

a = [1, 2, 3]
b = {'a': 1, 'b': 2, 'c': 'fdsafdsf'}

# import learn_function as lf # 模块 module

# lf.print_list(a)
# lf.print_dict(b)

# from learn_function import print_list as pl, print_dict as pd
# pl(a)
# pd(b)

from learn_function import *

fn = get_formatted_name_0('aaa', 'bbb')
print(fn)