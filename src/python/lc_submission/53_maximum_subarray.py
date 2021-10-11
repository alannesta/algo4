"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

import sys


# DP: dp[i] stands for maximum sum with nums[i] as the last element
def solution():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    def maxSubArray(nums) -> int:
        dp = []
        max_sum = -sys.maxsize

        for i in range(len(nums) + 1):
            dp.append(-sys.maxsize)

        dp[0] = 0

        for i in range(1, len(nums) + 1):
            dp[i] = max(dp[i - 1] + nums[i - 1], nums[i - 1])

            if max_sum < dp[i]:
                max_sum = dp[i]

        print(dp)

        return max_sum

    print(maxSubArray(nums))


# brute force
def solution2():
    n = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_s = -sys.maxsize
    pos = [-1, -1]

    for i in range(len(n)):
        s = n[i]
        # edge case when there is only on elem
        if s > max_s:
            max_s = s
            pos = [i]
        for j in range(i + 1, len(n)):
            s = s + n[j]
            if s > max_s:
                max_s = s
                pos = [i, j]

    return max_s, pos


# recursion
def solution3():
    n = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_s = -sys.maxsize

    def walk(i, nums):
        nonlocal max_s
        if i == 0:
            if nums[0] > max_s:
                max_s = nums[0]
            return nums[0]

        res = walk(i - 1, nums)

        cur = max(nums[i] + res, nums[i])

        if cur > max_s:
            max_s = cur

        return cur

    walk(len(n) - 1, n)

    return max_s


# solution()
# print(solution2())
print(solution3())
