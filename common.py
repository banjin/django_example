# coding:utf-8

import time

from functools import  wraps

def time_it(func):
    """
    时间装饰器
    :param func:
    :return:
    """
    @wraps
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, start - time.time())
        return result

    return wrapper
