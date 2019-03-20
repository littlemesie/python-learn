# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2018/10/5 16:22
@summary:
"""

_function = {}
def register(f):
    global _function
    _function[f.__name__] = f
    return f

@register
def foo():
    print(_function)
    return 'bar'

f = foo()
print(f)
