"""
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

from copy import copy


# debug helper
def print_indent(text, level):
    indent = level * '  '
    print(indent + text)
    # pass


# backtracking standard template
def solution1():
    solution = []
    memo = []
    n = 0

    def walk(nums, sub_selection):
        global n

        if len(nums) == len(sub_selection) and sorted(sub_selection) not in memo:
            solution.append(copy(sub_selection))
            memo.append(sorted(copy(sub_selection)))
            return

        if sorted(sub_selection) not in memo:
            solution.append(copy(sub_selection))
            memo.append(sorted(copy(sub_selection)))

        choices = list(set(nums) - set(sub_selection))

        for choice in choices:
            sub_selection.append(choice)
            walk(nums, sub_selection)
            sub_selection.remove(choice)

    print('begin......')
    walk([1, 2, 3], [])
    print(solution)


# 数学归纳法, explainable solution
def solution2():
    solution = []

    def walk(nums):
        if len(nums) == 0:
            solution.append([])
            return [[]]

        elem = nums.pop()
        subs = walk(nums)

        for i in range(len(subs)):
            solution.append(subs[i] + [elem])
            subs.append(subs[i] + [elem])

        return subs

    result = walk([1, 2, 3])

    print(result)
    print(solution)


# optimized solution tree, no duplicate nodes, do not need memo anymore
def solution3():
    solution = []

    def walk(nums, selection, idx):
        solution.append(copy(selection))

        if idx == len(nums):
            return

        for i in range(idx, len(nums)):
            selection.append(nums[i])
            walk(nums, selection, i + 1)
            selection.pop()

    walk([1, 2, 3], [], 0)
    print(solution)


# solution1()
solution2()
# solution3()
