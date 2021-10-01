"""
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


# standard DP solution
def solution1():
    def coinChange(coins, amount):
        dp = [-1] * (amount + 1)

        dp[0] = 0
        for i in range(amount + 1):
            for c in coins:
                if i - c < 0:
                    continue
                else:
                    if dp[i - c] == -1:
                        continue
                    else:
                        dp[i] = dp[i - c] + 1

        print(dp)

    coinChange([1, 2, 5], 11)


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


# solution1()
solution2()
