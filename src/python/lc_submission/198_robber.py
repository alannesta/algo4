"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.


Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""


# dp
def solution():
    # nums = [1, 2, 3, 1]
    nums = [2, 7, 9, 3, 1]
    m_amount = -1

    dp = []
    for i in range(len(nums) + 1):
        dp.append(-1)

    for i in range(len(nums) + 1):
        if i == 0:
            dp[i] = 0
        elif i == 1:
            dp[i] = nums[i - 1]
        else:
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        if dp[i] > m_amount:
            m_amount = dp[i]

    return m_amount


# recursion
def solution2():
    nums = [2, 7, 9, 3, 1]
    memo = {}

    def walk(i):
        if i in memo:
            return memo[i]

        # edge case is tricky
        if i == 0:
            memo[i] = nums[0]
            return nums[0]
        if i < 0:
            return 0

        val1 = walk(i - 1)
        val2 = walk(i - 2)

        memo[i - 1] = val1
        memo[i - 2] = val2

        return max(val1, val2 + nums[i])

    return walk(len(nums) - 1)


print(solution2())
print(solution())
