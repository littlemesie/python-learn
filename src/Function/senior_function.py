# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2019/3/20 23:49
@summary:
"""

def f(x):
    return x*x

def is_odd(n):
    return n % 2 == 1

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list(map(f, arr)))
    arr01 = [1, 2, 4, 5, 6, 9, 10, 15]
    print(list(filter(is_odd, arr01)))
    print(sorted([36, 5, -12, 9, -21], key=abs))