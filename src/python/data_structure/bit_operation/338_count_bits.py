"""
https://leetcode.com/problems/counting-bits/

"""
from typing import List


def count_bit(n):
    cnt = 0
    while n := n & (n - 1):
        cnt += 1
    return cnt


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            res.append(count_bit(i))

        return res

    # TODO: 此题应用动态规划来求解, 避免重复计算
    # 观察pattern
    # 思路: http://leetcode.jp/leetcode-338-counting-bits-%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF%E5%88%86%E6%9E%90/
    def countBitsV2(self, n):
        res = [0] * (n + 1)

        for i in range(n + 1):
            res[i] = i % 2 + res[i // 2]

        return res


print(Solution().countBits(17))
