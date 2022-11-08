"""
https://leetcode.com/problems/subsets-ii/

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""
from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()     # important!! needs to be sorted, see pic in notes
        self.traverse(nums, 0, [])
        return self.result

    def traverse(self, nums, start_index, cur_path):
        self.result.append(cur_path[:])

        level_visited = set()
        for i in range(start_index, len(nums)):
            if nums[i] in level_visited:
                continue

            cur_path.append(nums[i])
            level_visited.add(nums[i])
            self.traverse(nums, i + 1, cur_path)
            cur_path.pop()
