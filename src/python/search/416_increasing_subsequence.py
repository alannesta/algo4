"""
https://leetcode.com/problems/increasing-subsequences/

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

"""
from typing import List
from copy import copy


class Solution:
    def __init__(self):
        self.visited = {}
        self.results = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.traverse(nums, 0, [])
        return self.results

    def traverse(self, nums, start_index, cur_path: List[int]):
        # 同层级去重
        visited = set()

        if len(cur_path) > 1:
            self.results.append(copy(cur_path))

        for i in range(start_index, len(nums)):
            # 易错点: nums[i] >= nums[i-1] vs nums[i] >= cur_path[-1]
            if (cur_path and nums[i] < cur_path[-1]) or nums[i] in visited:
                continue
            visited.add(nums[i])
            cur_path.append(nums[i])
            self.traverse(nums, i + 1, cur_path)
            cur_path.pop()