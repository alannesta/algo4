import heapq

from data_structure.heap import Heap
from data_structure.heap.sliding_window_median import SlidingWindowMedian
from util import timeit, generate_random_integer_list

input = generate_random_integer_list(100 * 100 * 100, 100 * 100 * 100)


@timeit
def sliding_window_my_impl(input):
    sliding_window = SlidingWindowMedian(input, 1000)
    i = 0
    while i < 5000:
        sliding_window.slide()
        sliding_window.median()
        i += 1


@timeit
def sliding_window_bisect(input):
    sliding_window = SlidingWindowMedian(input, 1000)
    i = 0
    while i < 5000:
        sliding_window.slide_bisect()
        sliding_window.median()
        i += 1

sliding_window_bisect(input)
sliding_window_my_impl(input)
