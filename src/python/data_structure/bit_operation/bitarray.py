"""
implement bit array data structure using int

reference:
https://blog.csdn.net/weixin_39198406/article/details/107716579
https://github.com/ilanschnell/bitarray

"""
import math
import random


class BitMap:
    def __init__(self, max_num):
        """
        initialize bit array based on the maximum value that needs to be stored
        """
        self._size = math.ceil((max_num + 1) / 32)  # starting from 0, first 32 bits store 0...31
        self.bitarray = [0 for i in range(self._size)]  # each int is 32bit

    def set(self, num):
        bitarray_pos = num // 32
        bit_pos = num % 32

        self.bitarray[bitarray_pos] = self.bitarray[bitarray_pos] | (1 << bit_pos)

    def get(self, num):
        bitarray_pos = num // 32
        bit_pos = num % 32

        if self.bitarray[bitarray_pos] & (1 << bit_pos):
            return 1  # bit is set

        return 0


# Testcase
import time
import sys


def generate_random_integer_list(num_range, size):
    return random.choices(range(1, num_range), k=size)


bmp = BitMap(10 ** 6)
map = {}

data = generate_random_integer_list(10 ** 6, 10 ** 6)

for i in data:
    bmp.set(i)
    map[i] = True

# time.sleep(10)
print(1000 in data)
print(bmp.get(1000))
print(1000 in map)

print('bitmap size:', sys.getsizeof(bmp.bitarray))  # 253,624
print('dict size:', sys.getsizeof(map))  # 20,971,608
print('list size:', sys.getsizeof(data))
