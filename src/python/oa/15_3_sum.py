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


# 2022.11.09 refresh: convert to combination sum, exceed time limit because prune is not aggressive enough
class Solution2:
    def __init__(self):
        self.result = []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.traverse(nums, start_idx=0, target=0, cur_path=[])
        return self.result

    def traverse(self, nums, start_idx, target, cur_path):
        if len(cur_path) == 3:
            if target == 0:
                self.result.append(cur_path[:])
                return True
            return

        visited = set()
        for i in range(start_idx, len(nums)):
            if nums[i] in visited:
                continue

            cur_path.append(nums[i])
            visited.add(nums[i])
            if self.traverse(nums, i + 1, target - nums[i], cur_path):
                cur_path.pop()
                # termination on this level
                break
            cur_path.pop()


# n-sum的写法, 不明白为什么比combination sum的写法快那么多~~
class Solution3:
    def __init__(self):
        self.result = []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        searched = set()
        for i in range(len(nums)):
            if nums[i] in searched:
                continue
            searched.add(nums[i])
            self.result += self.n_sum(nums, n=3, target=0, start_index=i)
        return self.result

    def n_sum(self, nums, n, target, start_index):
        if n == 2:
            memo = set()
            tracker = {}
            result = []
            for num in nums[start_index:]:
                if num in tracker:
                    if (num, tracker[num]) not in memo:
                        result.append([num, tracker[num]])
                        memo.add((num, tracker[num]))
                else:
                    tracker[target - num] = num
            return result

        result_set = self.n_sum(nums, n - 1, target - nums[start_index], start_index + 1)

        return [[nums[start_index]] + res for res in result_set]
