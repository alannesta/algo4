"""
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
For example, If n = 4 and k = 2, a solution is:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
from copy import copy

"""
Solution 1:
backtrack暴力穷举, leetcode超时 combination(10, 5)
"""


def solution1():
    combos = []
    memo = []

    def combination(n, k):
        nums = [i + 1 for i in range(n)]

        walk(nums, selection=[], limit=k)

    def walk(nums, selection, limit):
        if len(selection) == limit and sorted(selection) not in memo:
            sel = copy(selection)
            combos.append(copy(selection))
            memo.append(sorted(sel))
            return

        choices = list(set(nums) - set(selection))

        for choice in choices:
            selection.append(choice)
            walk(nums, selection, limit)
            selection.pop()

    combination(5, 2)
    print(combos)


solution1()
