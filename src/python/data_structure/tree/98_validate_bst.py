"""
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.validate(root, root)

    def validate(self, node, parent) -> bool:
        if not node.left and not node.right:
            return True

        valid_left = valid_right = True

        if node.left:
            if node.left.val > node.val or node.left.val > parent.val:
                return False

            valid_left = self.validate(node.left, node)

        if node.right:
            if node.right.val < node.val or node.node.val < parent.val:
                return False
            valid_right = self.validate(node.right, node)

        return valid_left and valid_right
