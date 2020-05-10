from data_structure.heap.sliding_window_median import SlidingWindowMedian
from data_structure.heap.sliding_window_maximum import SlidingWindowMaximum, SlidingWindowMaximum_Deque
from util import timeit, generate_random_integer_list

input = generate_random_integer_list(100 * 100 * 100 * 100, 100 * 100 * 100)


@timeit
def sliding_window_my_impl(input):
    sliding_window = SlidingWindowMedian(input, 2000)
    i = 0
    while i < 2000:
        sliding_window.slide()
        sliding_window.median()
        i += 1


@timeit
def sliding_window_bisect(input):
    sliding_window = SlidingWindowMedian(input, 2000)
    i = 0
    while i < 2000:
        sliding_window.slide_bisect()
        sliding_window.median()
        i += 1



@timeit
def sliding_window_max_sort(input):
    sliding_window = SlidingWindowMedian(input, 2000)
    for i in range(0, 2000):
        sliding_window.slide()
        sliding_window.max()

@timeit
def sliding_window_max_pointer(input):
    sliding_window = SlidingWindowMaximum(input, 2000)
    for i in range(0, 3000):
        sliding_window.slide()
        sliding_window.max()

@timeit
def sliding_window_max_deque(input):
    sliding_window = SlidingWindowMaximum_Deque(input, 2000)
    for i in range(0, 3000):
        sliding_window.slide()
        sliding_window.max()


#################################
# Test group:
# sliding window median: std bisect vs hand written binary search
#################################
# sliding_window_bisect(input)
# sliding_window_my_impl(input)

###########################################
# Test group:
# sliding window maximum: resort vs pointer vs deque
###########################################
# sliding_window_max_sort(input)
sliding_window_max_pointer(input)
sliding_window_max_deque(input)