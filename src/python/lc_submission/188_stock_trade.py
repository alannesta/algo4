"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""


# unlimited transactions
def solution():
    nums = [3, 2, 6, 5, 0, 3]

    # nums = [7, 1, 5, 3, 6, 4]

    def walk(idx):
        if idx == 0:
            return 0
        if idx == 1:
            return max(nums[1] - nums[0], 0)

        diff = nums[idx] - nums[idx - 1]

        prof = walk(idx - 1)

        if diff > 0:
            return prof + diff

        return prof

    print(walk(len(nums) - 1))


# only one transaction
def solution2():
    nums = [7, 1, 5, 3, 6, 4]

    dp = []
    max_p = 0

    for i in range(len(nums)):
        dp.append(0)

    for i in range(len(nums)):
        if i == 0:
            continue

        diff = nums[i] - nums[i - 1]

        if diff > 0:
            dp[i] = dp[i - 1] + diff
        else:
            dp[i] = max(dp[i - 1] + diff, 0)

        if max_p < dp[i]:
            max_p = dp[i]

    return max_p





# solution()
# print(solution2())
