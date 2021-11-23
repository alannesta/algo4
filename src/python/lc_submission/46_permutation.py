"""
经典题目, 暴力美学, 百刷不厌

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

https://leetcode.com/problems/permutations/
"""

from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.dfs(nums)

    def dfs(self, nums):
        result = []

        if not nums:
            return [[]]

        if len(nums) == 1:
            return [nums]

        item = nums.pop()

        perms = self.dfs(nums)

        for perm in perms:
            # Essential: len + 1 here to generate all permutations
            for i in range(len(perm) + 1):
                result.append(perm[: i] + [item] + perm[i:])

        return result

    # 47 add memo to filter out duplicates
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        result = []

        if not nums:
            return [[]]

        if len(nums) == 1:
            return [nums]

        item = nums.pop()

        perms = self.permuteUnique(nums)

        for perm in perms:
            # Essential: len + 1 here to generate all permutations
            for i in range(len(perm) + 1):
                n_perm = perm[: i] + [item] + perm[i:]
                t_perm = tuple(n_perm)

                if t_perm in self.memo:
                    continue
                else:
                    result.append(n_perm)
                    self.memo[n_perm] = True

        return result
