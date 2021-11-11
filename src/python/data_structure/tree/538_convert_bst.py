"""
https://leetcode.com/problems/convert-bst-to-greater-tree/

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.sum = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root

    def traverse(self, node):
        if not node:
            return

        self.traverse(node.left)
        self.traverse(node.right)

        self.sum += node.val
        node.val = self.sum
