# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2018/10/2 21:41
@summary: 接口
"""

from abc import ABCMeta,abstractmethod

class Payment(metaclass=ABCMeta):

    #  定义一个接口
    @abstractmethod
    def pay(self,money):
        pass
