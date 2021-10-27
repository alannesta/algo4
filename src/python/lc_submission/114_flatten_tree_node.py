"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list
and the left child pointer is always null.

The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 32 ms, faster than 94.88% of Python3 online submissions for Flatten Binary Tree to Linked List.
    Memory Usage: 15.4 MB, less than 13.89% of Python3 online submissions for Flatten Binary Tree to Linked List.
    """
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        right_ptr = root.right
        root.right = root.left

        ptr = root.left
        while ptr.right:
            ptr = ptr.right

        ptr.right = right_ptr
