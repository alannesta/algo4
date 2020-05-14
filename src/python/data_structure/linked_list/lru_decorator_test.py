import random
import time
from functools import lru_cache
from util.timing import timeit
from data_structure.linked_list.lru_decorator import lru_cache_wrapper


@timeit
def test_lru_decorator():
    for i in range(0, 10):
        # super_heavy_computation(random.randint(0, 3), config={"key": "val"}) # ERROR: dict is not hashable!!
        super_heavy_computation(random.randint(0, 3), config="val") # dict is not hashable!!

@timeit
def test_custom_lru_decorator():
    for i in range(0, 10):
        ultra_heavy_computation(random.randint(0, 3), config="key")

@lru_cache(maxsize=5)
def super_heavy_computation(seed, config=None):
    time.sleep(1)
    return seed

@lru_cache_wrapper(cache_size=5)
def ultra_heavy_computation(seed, config=None):
    time.sleep(1)
    return seed

test_lru_decorator()
test_custom_lru_decorator()