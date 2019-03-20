# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2018/10/6 16:25
@summary:
"""
import pprint,requests

def main():
    response = requests.post(
        'http://127.0.0.1:5000/post',
        {'foo':'bar'}
    )

    pprint.pprint(response.json())

if __name__ == '__main__':
    main()