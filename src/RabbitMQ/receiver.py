# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2018/10/8 22:58
@summary:
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print('receive msg: %s' % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False)


print('waiting for msg...')
channel.start_consuming()
