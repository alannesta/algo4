"""
https://leetcode.com/problems/missing-number/
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cache = {}

        for i in range(len(nums) + 1):
            cache[i] = 1

        for i in nums:
            del cache[i]

        return list(cache.keys())[0]

    def missingNumber2(self, nums):
        return sum([i for i in range(len(nums) + 1)]) - sum(nums)

    def missingNumber3(self, nums):
        return set([i for i in range(len(nums) + 1)]) - set(nums)
