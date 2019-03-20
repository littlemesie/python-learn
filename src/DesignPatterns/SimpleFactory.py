# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2018/10/2 22:07
@summary:
"""

from abc import ABCMeta,abstractmethod

class Payment(metaclass=ABCMeta):

    # 抽象产品角色
    @abstractmethod
    def pay(self,money):
        pass



class AiliPay(Payment):

    # 具体产品角色
    def __init__(self,enable_yuebao=False):
        self.enable_yuebao = enable_yuebao

    def pay(self,money):
        if self.enable_yuebao:
            print('使用余额宝支付%s元'%money)
        else:
            print('使用支付宝支付%s元'%money)

class ApplePay(Payment):
    # 具体产品角色
    def pay(self,money):
        print('使用苹果支付支付%s元'%money)

class PaymentFactory:

    # 工厂角色
    def create_payment(self,method):
        if method == 'alipay':
            return AiliPay()
        elif method == 'yuebao':
            return AiliPay(True)
        elif method == 'applepay':
            return ApplePay()
        else:
            return NameError

p = PaymentFactory()
f = p.create_payment('yuebao')
f.pay(100)