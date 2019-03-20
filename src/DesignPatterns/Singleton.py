# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2018/10/2 21:57
@summary: 单例模式
"""

class Singleton(object):

    # 如果该类已经有了一个实例则直接返回,否则创建一个全局唯一的实例
    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance


class MyClass(Singleton):

    def __init__(self, name):
        if name:
            self.name = name

if __name__ == '__main__':
    mc = MyClass('mesie')
    print(mc.name)