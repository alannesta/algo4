import random
import functools
import time

def generate_random_integer_list(num_range, size):
    return random.choices(range(1, num_range), k=size)


def timeit(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        print('time used: ', time.time() - start)

    return wrapper
