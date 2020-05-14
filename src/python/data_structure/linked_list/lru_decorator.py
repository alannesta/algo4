"""
impl funtionality similar to functool.lru_cache
"""
from collections import namedtuple
from functools import wraps, partial
from data_structure.linked_list.lru_cache import lru


def lru_cache_impl(fn, cache_size=10):
    cache = lru(cache_size)

    @wraps(fn)
    def wrapper(*args, **kwargs):
        print('call args:', args)
        print('current cache: ', cache.cache_lookup)
        cache_key = _make_key(args, kwargs, typed=False)
        cached = cache.get(cache_key)
        if cached is None:
            result = fn(*args, **kwargs)
            cache.set(cache_key, result)

            return result
        print('!!!cache hit!!!')
        return cached

    return wrapper


def lru_cache_wrapper(cache_size):
    return partial(lru_cache_impl, cache_size=cache_size)


# heavily "inspired" by code from std lib
def _make_key(args, kwds, typed,
              kwd_mark=(object(),),
              fasttypes={int, str, frozenset, type(None)},
              tuple=tuple, type=type, len=len):
    """Make a cache key from optionally typed positional and keyword arguments

    The key is constructed in a way that is flat as possible rather than
    as a nested structure that would take more memory.

    If there is only a single argument and its data type is known to cache
    its hash value, then that argument is returned without a wrapper.  This
    saves space and improves lookup speed.

    """
    key = args
    if kwds:
        key += kwd_mark
        for item in kwds.items():
            key += item
    if typed:
        key += tuple(type(v) for v in args)
        if kwds:
            key += tuple(type(v) for v in kwds.values())
    elif len(key) == 1 and type(key[0]) in fasttypes:
        return key[0]
    return _HashedSeq(key)
    # return key


_CacheInfo = namedtuple("CacheInfo", ["hits", "misses", "maxsize", "currsize"])


class _HashedSeq(list):
    """ This class guarantees that hash() will be called no more than once
        per element.  This is important because the lru_cache() will hash
        the key multiple times on a cache miss.

    """

    __slots__ = 'hashvalue'

    def __init__(self, tup, hash=hash):
        self[:] = tup
        self.hashvalue = hash(tup)

    def __hash__(self):
        return self.hashvalue


# @lru_cache_impl
# def test_fn(*args, **kwargs):
#     print('args: ', args)
#     print('kwargs: ', kwargs)
#
#
# test_fn(1, 2, 3, key='value', value='key')

# print(_make_key((1,2,3), {'key': 'value', 'value': 'key'}, typed=False))
