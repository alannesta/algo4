"""
https://leetcode.com/problems/coin-change/
You are given an integer array coins representing coins of different denominations and
an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""
import sys
from collections import deque


# DP solution, one dimension
def solution1_a():
    def coinChange(coins, amount):
        dp = []
        for i in range(amount + 1):
            dp.append(-1)

        for i in range(amount + 1):
            if i == 0:
                dp[i] = 0
                continue
            for c in coins:
                if i - c < 0:
                    continue
                if dp[i - c] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i - c] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[amount]

    print(coinChange([1, 2, 5], 11))


# DP solution, two dimension state(knapsack template)
def solution1_b():
    def coinChange(coins, amount):
        d_amount = amount + 1
        d_coin = len(coins) + 1

        dp = []

        for i in range(d_coin):
            tmp = []
            for j in range(d_amount):
                if j == 0:
                    tmp.append(0)  # initialize state, when amount is 0, 0 coins is required
                else:
                    tmp.append(-1)  # -1 stands for no solution

            dp.append(tmp)

        # loop order is different from above
        # we derive state by "column", not by "row"
        for j in range(d_amount):
            for i in range(d_coin):
                if i == 0:
                    continue
                if j - coins[i - 1] < 0:  # compensate for index offset
                    dp[i][j] = dp[i - 1][j]
                else:
                    if dp[i - 1][j] == -1:
                        if dp[i][j - coins[i - 1]] == -1:
                            dp[i][j] = -1
                        else:
                            dp[i][j] = dp[i][j - coins[i - 1]] + 1
                    else:
                        if dp[i][j - coins[i - 1]] == -1:
                            dp[i][j] = dp[i - 1][j]
                        else:
                            dp[i][j] = min(dp[i][j - coins[i - 1]] + 1, dp[i - 1][j])

        min_c = sys.maxsize

        for i in range(1, d_coin):
            if dp[i][amount] == -1:
                continue
            if dp[i][amount] < min_c:
                min_c = dp[i][amount]

        if min_c == sys.maxsize:
            return -1

        return min_c

    print(coinChange([1, 2, 5], 11))


# backtracking, exceeds time limit even with memo
def solution2():
    c = [1, 2, 5]
    amount = 11
    memo = {}

    def walk(coins, path, target):
        key = tuple(sorted(path)) + (target,)
        if key in memo:
            return memo[key]

        if target < 0:
            memo[key] = -1
            return -1

        if target == 0:
            memo[key] = len(path)
            return len(path)

        res = []

        for coin in coins:
            path.append(coin)
            count = walk(coins, path, target - coin)
            if count != -1:
                res.append(count)
            path.pop()

        return min(res) if res else -1

    print(walk(c, [], amount))


# solution3 BFS (faster than dp solution)
def solution3():
    queue = deque()
    visited = set()
    coins = [1, 2, 5]
    amount = 11
    step = 0

    queue.appendleft(amount)

    while queue:
        for i in range(len(queue)):
            target = queue.pop()
            if target == 0:
                return step

            for coin in coins:
                new_target = target - coin
                if new_target >= 0 and new_target not in visited:
                    visited.add(new_target)
                    queue.appendleft(new_target)

        step = step + 1

    return -1


# solution1_a()
solution1_b()
# solution2()

# print(solution3())
