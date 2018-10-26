# -*- coding: utf-8 -*-
import os
import pickle

from .hash_wrap import md5


YCACHE_ROOT_DIR = os.getenv('YCACHE_ROOT_DIR', '.ycache-data')


def cache_key(f, *args, **kwargs):

    if not os.path.exists(YCACHE_ROOT_DIR):
        os.makedirs(YCACHE_ROOT_DIR)

    s = '%s-%s-%s' % (f.__name__, str(args), str(kwargs))
    return os.path.join(YCACHE_ROOT_DIR, '%s.p' % md5(s))


def cache(f):
    def wrap(*args, **kwargs):
        fn = cache_key(f, *args, **kwargs)
        if os.path.exists(fn):
            # print('loading cache')
            with open(fn, 'rb') as fr:
                return pickle.load(fr)

        obj = f(*args, **kwargs)
        with open(fn, 'wb') as fw:
            pickle.dump(obj, fw)
        return obj

    return wrap


@cache
def add(a, b):
    return a + b


if __name__ == '__main__':
    print(add(3, 4))
    print(add(3, 4))
    print(add(8, 4))
    print(add(4, 8))
