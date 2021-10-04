"""
https://leetcode.com/problems/partition-equal-subset-sum/
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets
such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
"""


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


print(solution())
