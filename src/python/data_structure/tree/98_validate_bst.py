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
    def __init__(self):
        self.prev = None
        self.invalid = False   # marker to stop recursion early

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return self.validate(root, None, None)
        return self.validate_v2(root)

    def validate(self, node, min_val, max_val) -> bool:
        if not node:
            return True

        if max_val and node.val >= max_val.val:
            return False

        if min_val and node.val <= min_val.val:
            return False

        return self.validate(node.left, min_val, node) and self.validate(node.right, node, max_val)

    def validate_v2(self, node) -> bool:
        """
        using in-order traversal.
        利用二叉树in-order traversal是升序遍历的性质, 引入一个额外的变量记录前值
        这个解法更容易理解
        :param node:
        :return:
        """

        if not node:
            return True

        if self.invalid:
            return False

        valid_l = self.validate_v2(node.left)

        if not self.prev:
            self.prev = node
        else:
            if node.val <= self.prev.val:
                self.invalid = True
                return False
            else:
                self.prev = node

        valid_r = self.validate_v2(node.right)

        return valid_l and valid_r
