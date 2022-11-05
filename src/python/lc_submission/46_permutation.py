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


# 2022.11.05 update: 更新permutation I, II backtracking的写法
class Solution2:

    def __init__(self):
        self.result = []
        self.used = None

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.used = [0] * len(nums)
        self.traverse(nums, [])

        return self.result

    def traverse(self, nums, cur_path):
        if len(cur_path) == len(nums):
            self.result.append(cur_path[:])
            return

        for i in range(len(nums)):
            if self.used[i]:
                continue

            cur_path.append(nums[i])
            self.used[i] = 1
            self.traverse(nums, cur_path)
            self.used[i] = 0
            cur_path.pop()

    # LC47: 解法的关键在于去重:
    # 1. permutation没有start_index来避免重复访问, 所以需要used[] 数组来对所有元素做标记去重
    # 2. 解空间树的同一层没必要从一个相同的元素开始, traverse方法内部使用set去重
    # 3. 以上这两种去重都实现了提前剪枝, 效率上比在最终插入结果集(result.append())时再进行去重判断高很多
    # 详细分析: https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E5%8E%BB%E9%87%8D%E9%97%AE%E9%A2%98%E7%9A%84%E5%8F%A6%E4%B8%80%E7%A7%8D%E5%86%99%E6%B3%95.md
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.used = [0] * len(nums)
        self.traverseUnique(nums, [])
        return self.result

    def traverseUnique(self, nums, cur_path):
        if len(cur_path) == len(nums):
            self.result.append(cur_path[:])
            return

        picked = set()
        for i in range(len(nums)):
            if self.used[i] or nums[i] in picked:
                continue

            cur_path.append(nums[i])
            picked.add(nums[i])
            self.used[i] = 1
            self.traverseUnique(nums, cur_path)
            self.used[i] = 0
            cur_path.pop()
