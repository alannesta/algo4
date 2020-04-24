import random
import functools
import time

from data_structure.heap import Heap


def generate_random_integer_list(num_range, size):
    return random.choices(range(1, num_range), k=size)


def timeit(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        print('time used: ', time.time() - start)

    return wrapper


# print(generate_random_integer_list(30, 10))

@timeit
def heapify_perf(input):
    ma_heap = Heap()
    ma_heap.heapify(input)
    # print(ma_heap._heap_arr)


input = generate_random_integer_list(100 * 100 * 100 * 100 * 100, 10000)

heapify_perf(input)
