# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2018/10/6 16:25
@summary:
"""
import pprint,requests,json

def main():
    # 需要指明Content-Type
    response = requests.post(
        'http://127.0.0.1:5000/post',
        json.dumps({'foo':'bar'}),
        headers={'Content-Type':'application/json'}
    )

    pprint.pprint(response.json())

if __name__ == '__main__':
    main()