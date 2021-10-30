"""
https://leetcode.com/problems/maximum-binary-tree/

You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively
from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        idx = nums.index(max(nums))

        node = TreeNode(nums[idx])

        left = nums[0:idx]
        # the good thing about python is there will not be index out of range error when slicing
        right = nums[idx + 1:]

        node.left = self.constructMaximumBinaryTree(left)
        node.right = self.constructMaximumBinaryTree(right)

        return node
