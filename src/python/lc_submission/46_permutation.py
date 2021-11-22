"""
经典题目, 暴力美学, 百刷不厌

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

https://leetcode.com/problems/permutations/
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.dfs(nums)

    def dfs(self, nums):
        result = []

        if len(nums) == 1:
            return [nums]

        item = nums.pop()

        perms = self.dfs(nums)

        for perm in perms:
            # Essential: len + 1 here to generate all permutations
            for i in range(len(perm) + 1):
                result.append(perm[: i] + [item] + perm[i:])

        return result
