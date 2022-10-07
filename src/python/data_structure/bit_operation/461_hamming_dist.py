"""
https://leetcode.com/problems/hamming-distance/
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y  # XOR, 相同bit结果为0,不同bit结果为1
        cnt = 0
        while res != 0:
            res = res & (res - 1)
            cnt += 1

        return cnt
