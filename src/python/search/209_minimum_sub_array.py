"""
https://leetcode.com/problems/minimum-size-subarray-sum/

"""

from typing import List


class Solution:
    def __init__(self):
        self.min_length = 2 ** 31 - 1
        self.visited = {}

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        self.traverse(target, nums, start_index=0, cur_path=[])
        return self.min_length

    def traverse(self, target, nums, start_index, cur_path):
        if target <= 0:
            self.min_length = min(len(cur_path), self.min_length)

        if len(cur_path) > self.min_length:
            return

        for i in range(start_index, len(nums)):
            cur_path.append(nums[i])
            self.traverse(target - nums[i], nums, i + 1, cur_path)
            cur_path.pop()
