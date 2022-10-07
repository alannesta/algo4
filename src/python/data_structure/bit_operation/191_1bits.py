"""
https://leetcode.com/problems/number-of-1-bits/

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        test = 1
        cnt = 0
        for i in range(32):
            if n & test != 0:
                cnt = cnt + 1
            test = test << 1
        return cnt

    def hammingWeight2(self, n: int) -> int:
        str_rep = bin(n)
        cnt = 0
        for char in str_rep:
            if char == '1':
                cnt += 1

        return cnt

    def hammingWeight3(self, n: int) -> int:
        # https://mirrors.gitcode.host/labuladong/fucking-algorithm/think_like_computer/CommonBitManipulation.html
        cnt = 0
        while n != 0:
            n = n & (n - 1)
            cnt += 1

        return cnt

print(Solution().hammingWeight3(0b10101111))
# print(Solution().hammingWeight(0b10101111))
