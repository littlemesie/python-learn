# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2018/10/2 21:44
@summary: 实现接口
"""
from src.DesignPatterns import Payment

class AiliPay(Payment):

    def pay(self,money):
        print('使用支付宝支付%s元' % money)

if __name__ == '__main__':
    ap = AiliPay()
    ap.pay(20)