"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed)
of all the values of the nodes in the tree.

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.counter = 0
        self.target = 0
        self.val = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.target = k
        self.traverse(root)

        return self.val

    def traverse(self, node):
        if node is None:
            return

        self.traverse(node.left)
        self.counter += 1
        if self.counter == self.target:
            self.val = node.val
            return
        self.traverse(node.right)
