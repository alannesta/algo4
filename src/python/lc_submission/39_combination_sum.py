"""
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""


def solution():
    input_ = [2, 3, 6, 7]
    ans = []
    memo = {}

    def walk(nums, path, target):
        if sum(path) > target:
            return

        if sum(path) == target and tuple(sorted(path)) not in memo:
            ans.append(path[:])
            memo[tuple(sorted(path))] = True
            return

        for i in range(len(nums)):
            path.append(nums[i])
            walk(nums, path, target)
            path.pop()

    walk(input_, [], 7)

    print(ans)


def solution2():
    input_ = [2, 3, 6, 7]
    ans = []
    memo = {}

    def walk(nums, path, target, start_pos):
        if target < 0:
            return

        sorted_p = tuple(sorted(path))
        if target == 0 and sorted_p not in memo:
            ans.append(path[:])
            memo[sorted_p] = True
            return

        for i in range(start_pos, len(nums)):
            path.append(nums[i])
            walk(nums, path, target - nums[i], i)
            path.pop()

    walk(input_, [], 7, 0)

    print(ans)


# solution()
# solution2()

from typing import List


# 2022.10.19 更新: 不需要memo的解法:
class Solution:
    def __init__(self):
        self.result = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.traverse(candidates, 0, target=target, cur_path=[])
        return self.result

    def traverse(self, nums, start_idx, target, cur_path):
        if start_idx >= len(nums):
            return

        if target == 0:
            self.result.append(cur_path[::])  # copy of cur_path
            return

        if target < 0:
            return

        for idx in range(start_idx, len(nums)):
            cur_path.append(nums[idx])
            self.traverse(nums, idx, target - nums[idx], cur_path)  # 选取重复元素的关键点: start_pos idx不要+1
            cur_path.pop()

# lc40: combination sumII
class Solution2:
    def __init__(self):
        self.result = []
        self.memo = {}
        self.iter = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.traverse(candidates, 0, target=target, cur_path=[])
        return self.result

    def traverse(self, nums, start_idx, target, cur_path):
        # 这道题目memo的设计是关键
        # 因为只需要找到不重复的subset, 所以memo的check可以放在这里
        # 后面如果有和nums[0]重复的元素, 其后面的search都可以skip, 因为first pass会穷尽其所有的可能性

        # key = "".join(map(lambda x: str(x), sorted(cur_path)))
        key = tuple(sorted(cur_path))
        # why we need to check memo here?
        # will there be duplicates?
        if key in self.memo:
            return
        else:
            self.memo[key] = True

        if target == 0:
            # self.memo[key] = True
            self.result.append(cur_path[::])  # copy of cur_path
            return

        if target < 0:
            return

        self.iter += 1

        for idx in range(start_idx, len(nums)):
            cur_path.append(nums[idx])
            self.traverse(nums, idx + 1, target - nums[idx], cur_path)
            cur_path.pop()


input = [1, 1, 1, 2, 3, 1, 1]

sol = Solution2()
print(sol.combinationSum2(input, target=5))
print(sol.iter)
