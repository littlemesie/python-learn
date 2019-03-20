# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2018/10/5 16:40
@summary:
"""
import functools,inspect

def check_is_admin(func):
    @functools.wraps(func)

    def wrapper(*args,**kwargs):
        func_args = inspect.getcallargs(func,*args,**kwargs)

        if func_args.get('username') != 'admin':
            raise Exception('This user is not allowed to get food')
        return func(*args,**kwargs)
    return wrapper

class Store(object):

    @check_is_admin
    def get_food(self,username,food):
        return self.get(food)

    @check_is_admin
    def put_food(self, username, food):
        return self.put(food)

    def get(self,food):
        return food

    def put(self,food):
        return food

if __name__ == '__main__':
    s = Store()
    food = s.get_food(**{'username': 'admin'}, food='apple')
    print(food)