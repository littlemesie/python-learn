# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2019/3/30 22:56
@summary:
"""

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)
print(list(filter(lambda n: n % 2 == 1, range(1, 20))))