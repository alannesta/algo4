"""
40. Combination Sum II
https://leetcode.com/problems/combination-sum-ii/
"""
from typing import List


# 2022.11.08 refresh previous solution with another way of prune the result
class Solution:
    def __init__(self):
        self.result = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # essential: must sort to use level_visited filter
        self.traverse(candidates, 0, target=target, cur_path=[])
        return self.result

    def traverse(self, nums, start_idx, target, cur_path):
        if target < 0:
            return

        if target == 0:
            self.result.append(cur_path[:])
            return

        level_visited = set()

        for i in range(start_idx, len(nums)):
            if nums[i] in level_visited:
                continue
            cur_path.append(nums[i])
            level_visited.add(nums[i])
            self.traverse(nums, i + 1, target - nums[i], cur_path)
            cur_path.pop()
