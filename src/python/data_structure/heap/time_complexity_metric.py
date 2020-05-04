import heapq

from data_structure.heap import Heap
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

input = generate_random_integer_list(100 * 100 * 100 * 100 * 100, 100 * 100 * 100)
# input = generate_random_integer_list(50, 10)

# heapify_perf(input)
heapify_perf_optimize(input)
# heapify_perf_v2(input)

# std_heapify(input)