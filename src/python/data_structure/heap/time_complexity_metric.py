import heapq

from data_structure.heap import Heap
from data_structure.heap.find_median import MedianFinder_Bruce, MedianFinder
from util import timeit, generate_random_integer_list

# print(generate_random_integer_list(30, 10))

@timeit
def heapify_perf(input):
    ma_heap = Heap()
    ma_heap.heapify(input)
    # print(ma_heap._heap_arr)

@timeit
def heapify_perf_optimize(input):
    ma_heap = Heap()
    ma_heap.heapify_optimize(input)
    # print(ma_heap._heap_arr)

@timeit
def heapify_perf_v2(input):
    ma_heap = Heap()
    ma_heap._heap_arr = input
    ma_heap.heapify_v2()
    # print(ma_heap._heap_arr)


@timeit
def std_heapify(input):
    heapq.heapify(input)


@timeit
def find_median_test(input):
    median_finder = MedianFinder()
    for i in input:
        median_finder.add_number(i)
        median_finder.median()


@timeit
def find_median_brute_force_test(input):
    median_finder = MedianFinder_Bruce()
    for i in input:
        median_finder.add_number(i)
        median_finder.median()

input = generate_random_integer_list(100 * 100 * 100 * 100, 100 * 100 * 10)
# input = generate_random_integer_list(50, 10)

# heapify_perf(input)
# heapify_perf_optimize(input)
# heapify_perf_v2(input)

# std_heapify(input)


find_median_test(input)
# find_median_brute_force_test(input)