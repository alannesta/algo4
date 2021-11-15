"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and

inorder is the inorder traversal of the same tree, construct and return the binary tree.

"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # return self.build(preorder, inorder)
        return self.build_v2(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)

    def build(self, preorder, inorder):
        if not preorder:
            return None

        head_val = preorder[0]
        head_node = TreeNode(val=head_val)

        idx = inorder.index(head_val)

        left_tree = inorder[:idx]
        right_tree = inorder[idx + 1:]

        # slice preorder list into two parts based on the length of left and right subtree
        # exclude the first element
        head_node.left = self.build(preorder[1:len(left_tree) + 1], left_tree)
        head_node.right = self.build(preorder[len(left_tree) + 1:], right_tree)

        return head_node

    def build_v2(self, preorder, inorder, p_start, p_end, i_start, i_end):

        """
        using index instead of slice, this will usually be faster and save a lot of memory

        """
        if p_end < p_start:
            return None

        head_val = preorder[p_start]
        head_node = TreeNode(val=head_val)

        idx = inorder.index(head_val)

        # left_tree = inorder[i_start: idx]
        # right_tree = inorder[idx + 1: i_end]

        # slice preorder list into two parts based on the length of left and right subtree
        # exclude the first element
        head_node.left = self.build_v2(preorder, inorder, p_start + 1, p_start + idx - i_start, i_start, idx - 1)
        head_node.right = self.build_v2(preorder, inorder, p_start + 1 + idx - i_start, p_end, idx + 1, i_end)

        return head_node
