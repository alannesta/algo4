"""
Given an integer n, return the number of structurally unique BST's (binary search trees)
which has exactly n nodes of unique values from 1 to n.

https://leetcode.com/problems/unique-binary-search-trees/
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    solution to return total number of unique binary trees
    """

    def __init__(self):
        self.memo = {}  # use a memo to

    def numTrees(self, n: int) -> int:
        l = [i + 1 for i in range(n)]
        return self.construct(l)

    def construct(self, arr: List[int]) -> int:
        if not arr:
            return 1

        if len(arr) == 1:
            return 1

        if tuple(arr) in self.memo:
            return self.memo[tuple(arr)]

        total = 0

        for idx, elem in enumerate(arr):
            left = self.construct(arr[:idx])
            right = self.construct(arr[idx + 1:])

            total += left * right

        self.memo[tuple(arr)] = total

        return total


class Solution2:
    def __init__(self):
        self.trees = []
        self.memo = {}

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        l = [i + 1 for i in range(n)]
        return self.construct(l)

        # return self.trees

    def construct(self, arr: List[int]) -> Optional[List[TreeNode]]:
        trees = []

        if not arr:
            # this will greatly simplify if checks
            trees.append(None)
            return trees

        if tuple(arr) in self.memo:
            return self.memo[tuple(arr)]


        for idx, elem in enumerate(arr):

            left_nodes = self.construct(arr[:idx])
            right_nodes = self.construct(arr[idx + 1:])

            self.memo[tuple(arr[:idx])] = left_nodes
            self.memo[tuple(arr[idx + 1:])] = right_nodes

            # if checks that could be simplified via smarter return value
            # if not left_nodes and not right_nodes:
            #     root = TreeNode(val=elem)
            #     trees.append(root)
            #
            # if not left_nodes and right_nodes:
            #     for rn in right_nodes:
            #         root = TreeNode(val=elem, left=None)
            #         root.right = rn
            #         trees.append(root)
            #
            # if not right_nodes and left_nodes:
            #     for ln in left_nodes:
            #         root = TreeNode(val=elem, right=None)
            #         root.left = ln
            #         trees.append(root)

            if left_nodes and right_nodes:
                for ln in left_nodes:
                    for rn in right_nodes:
                        root = TreeNode(val=elem)
                        root.left = ln
                        root.right = rn
                        trees.append(root)

        return trees
