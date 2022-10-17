"""
preorder traversal using stack
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = []
        self.stack = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return self.result

        self.stack.append(root)

        while self.stack:
            node = self.stack.pop()
            self.result.append(node.val)
            if node.right:
                self.stack.append(node.right)
            if node.left:
                self.stack.append(node.left)

        return self.result


