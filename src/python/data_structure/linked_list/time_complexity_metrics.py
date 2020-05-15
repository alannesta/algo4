from util import timeit, generate_random_integer_list
from data_structure.linked_list.lru_cache import lru_custom_deque, lru, lru_ordered_dict, lru_final_evolution

cache_size = 1000
input_range = 10000

rand_input = generate_random_integer_list(num_range=input_range, size=input_range)


@timeit
def test_lru(cache):
    import random
    random.seed(100)
    for i in range(0, 1000000):
        idx = random.randint(0, input_range)
        cache.get(idx)

    for i in range(0, 1000000):
        idx = random.randint(0, input_range)
        cache.set(idx, idx)


cache1 = lru(cache_size)
for i in range(0, cache_size):
    cache1.set(rand_input[i], rand_input[i])

cache2 = lru_ordered_dict(cache_size)
for i in range(0, cache_size):
    cache2.set(rand_input[i], rand_input[i])

cache3 = lru_custom_deque(cache_size)
for i in range(0, cache_size):
    cache3.set(rand_input[i], rand_input[i])

cache4 = lru_final_evolution(cache_size)
for i in range(0, cache_size):
    cache3.set(rand_input[i], rand_input[i])

test_lru(cache1)
test_lru(cache2)
test_lru(cache3)
test_lru(cache4)
