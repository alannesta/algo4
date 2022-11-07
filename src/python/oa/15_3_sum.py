"""
2022.11.05 daily practice, revisit classic


"""
from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        tested = set()
        nums.sort()
        for i in range(len(nums)):
            if nums[i] in tested:
                continue
            tested.add(nums[i])
            two_sum_tup = self.twoSum(nums[i + 1:], 0 - nums[i])

            if two_sum_tup:
                for res in two_sum_tup:
                    result.append([nums[i], res[0], res[1]])

        return result

    def twoSum(self, nums, target):
        visited = {}
        result = []
        for i in range(len(nums)):
            if nums[i] in visited:
                result.append((nums[i], visited[nums[i]]))
            else:
                visited[target - nums[i]] = nums[i]

        return result
