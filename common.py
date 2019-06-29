# coding:utf-8

import time
from collections import OrderedDict
from functools import  wraps
# from functools import lru_cache 已经是标准库中的一部分

def time_it(func):
    """
    时间装饰器
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, start - time.time())
        return result

    return wrapper


############# 缓存器 ############################
class LRUCacheDict:
    def __init__(self, max_size=1024, expiration=60):
        """
        最大容量是1024个key,每个key的有效期为60s
        :param max_size:
        :param expiration:
        """
        self.max_size = max_size
        self.expiration = expiration
        self._cache = {}
        self._access_records = OrderedDict() # 记录访问时间
        self._expire_records = OrderedDict() # 记录生效时间


    def __setitem__(self, key, value):
        now = int(time.time())
        self.__delete__(key)

        self._cache[key] = value
        self._expire_records[key] = now + self.expiration
        self._access_records[key] = now

        self.cleanup()

    def __getitem__(self, key):
        now = int(time.time())
        del self._access_records[key]
        self._access_records[key] = now
        self.cleanup()
        return self._cache[key]

    def __contains__(self, key):
        self.cleanup()
        return key in self._cache

    def __delete__(self, key):
        if key in self._cache:
            del self._cache[key]
            del self._access_records[key]
            del self._expire_records[key]

    def cleanup(self):
        if self.expiration is None:
            return None
        pending_delete_keys = []
        now = int(time.time())
        # 删除 已经过期的缓存
        for k, v in self._expire_records.items():
            if v < now:
                pending_delete_keys.append(k)
        for del_k in pending_delete_keys:
            self.__delete__(del_k)
        # 如果数据量大于 max_size， 则删掉最旧的缓存
        while len(self._cache) > self.max_size:
            for k in self._access_records:
                self.__delete__(k)
                break



def cache_it(max_size=1024, expiration=60):
    CACHE = LRUCacheDict(max_size=max_size, expiration=expiration)

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            key = repr(*args, **kwargs)
            try:
                result = CACHE[key]
            except KeyError as e:
                result = func(*args, **kwargs)

                CACHE[key] = result
            return result
        return inner
    return wrapper

############ 合并对象列表 ##########

def my_reduce(func,seq, initial=None):
    if initial != None:
        ret = initial
    else:
        ret = seq.pop(0)
    for i in seq:
        ret = func(ret, i)
    return ret

querys_set_1 = 'filter列表对象'
querys_set_2 = 'filter列表对象'
temp_list = [querys_set_1, querys_set_2]

tickets = my_reduce(lambda x,y: x|y, temp_list)