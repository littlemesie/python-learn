# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2018/10/8 21:17
@summary: python 协成
"""

import time

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[consumer] consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'

def produce(c):
    c.__next__()
    n = 0
    while n < 5:
        n = n + 1
        print('[produce] producing %s...' % n)
        r = c.send(n)
        print('[produce] consumer return: %s' % r)
    c.close()

if __name__=='__main__':
    c = consumer()
    produce(c)