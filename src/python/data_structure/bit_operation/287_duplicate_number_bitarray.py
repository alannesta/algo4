"""
https://leetcode.com/problems/find-the-duplicate-number/

using bit array(map)
"""
import math
from typing import List

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


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bmp = BitMap(len(nums) - 1)
        for i in nums:
            if bmp.get(i) == 1:
                return i
            else:
                bmp.set(i)
