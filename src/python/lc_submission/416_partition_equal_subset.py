"""
https://leetcode.com/problems/partition-equal-subset-sum/
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets
such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
"""


# brute force v1, will exceed time limit
def solution():
    n = [1, 5, 11, 5, 2]
    memo = {}
    nums = sorted(n)

    def partition(nums, diff):
        if tuple(nums) + (diff,) in memo:
            return memo[tuple(nums) + (diff,)]
        if sum(nums) == diff:
            return True

        for i in range(len(nums)):
            target_diff = diff + nums[i]
            removed = nums.pop(i)
            r = partition(nums, target_diff)
            if r:
                return r
            memo[tuple(nums) + (diff,)] = r
            nums.insert(i, removed)

        return False

    return partition(nums, 0)


# brute force v2: convert to combination sum
def solution2():
    pass


# convert to dp[knapsack problem], find if there are items that sum up to sum(nums)/2
def solution3():
    n = [1, 5, 11, 5]
    if sum(n) % 2 == 1:
        return False
    total = sum(n) // 2

    l = total + 1
    dp = []
    for i in range(len(n) + 1):
        tmp = []
        for j in range(l):
            tmp.append(False)
        dp.append(tmp)

    dp[0][0] = True
    for j in range(len(n) + 1):
        for i in range(l):
            if i == 0 or j == 0:
                continue

            if i - n[j - 1] < 0:
                dp[j][i] = dp[j - 1][i]
            else:
                dp[j][i] = dp[j - 1][i - n[j - 1]] or dp[j - 1][i]

    print(dp)


solution3()

from typing import List
# 2022.10.19 update: 虽然依然会超时, 但是应该是回溯的最优写法了
class Solution:
    def __init__(self):
        self.total = None
        self.visited = {}

    def canPartition(self, nums: List[int]) -> bool:
        # nums.sort()
        self.total = sum(nums)
        if sum(nums) % 2 != 0:
            return False
        return self.traverse(nums, 0, cur_idx=[])

    def traverse(self, nums, idx, cur_idx):
        key = tuple(sorted(cur_idx))
        if key in self.visited:
            return False
        else:
            self.visited[key] = True

        if idx >= len(nums):
            return False

        cur_sum = sum(cur_idx)

        if cur_sum == self.total / 2:
            return True

        if cur_sum > self.total / 2:
            return False

        for i in range(idx, len(nums)):
            cur_idx.append(nums[i])
            if self.traverse(nums, i + 1, cur_idx):
                return True
            cur_idx.pop()

        return False
