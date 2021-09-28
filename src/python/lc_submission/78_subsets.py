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
    # indent = level * '  '
    # print(indent + text)
    pass


# backtracking standard template
def solution1():
    solution = []
    memo = []
    n = 0

    def walk(nums, sub_selection):
        global n

        if len(nums) == len(sub_selection) and sorted(sub_selection) not in memo:
            solution.append(copy(sub_selection))
            memo.append(sorted(sub_selection))
            return

        sel = copy(sub_selection)

        if sorted(sub_selection) not in memo:
            solution.append(sel)
            memo.append(sorted(sel))
        choices = list(set(nums) - set(sel))

        for choice in choices:
            sel.append(choice)
            walk(nums, sel)
            sel.remove(choice)

    print('begin......')
    walk([1, 2, 3], [])
    print(solution)


# optimized solution tree, no duplicate nodes, do not need memo anymore
def solution3():
    solution = []

    def walk(nums, selection, idx):
        sel = copy(selection)
        solution.append(selection)

        if idx == len(nums):
            return

        # sel = copy(selection)

        for i in range(idx, len(nums)):
            sel.append(nums[i])
            walk(nums, sel, i + 1)
            sel.pop()

    walk([1, 2, 3], [], 0)
    print(solution)


def subsets():
    result = []

    def backtrack(nums, start, path):
        result.append(path[:])

        if start == len(nums):
            return

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(nums, i + 1, path)
            path.pop()

    backtrack([1, 2, 3], 0, [])

    print(result)


# solution1()
solution3()
subsets()
