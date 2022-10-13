"""
https://leetcode.com/problems/merge-two-binary-trees/

"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        return self.merge(root1, root2)

    def merge(self, tree1, tree2):
        if not tree1:
            return tree2
        if not tree2:
            return tree1

        new_tree = TreeNode(val=tree1.val + tree2.val)
        new_tree.left = self.merge(tree1.left, tree2.left)
        new_tree.right = self.merge(tree1.right, tree2.right)

        return new_tree

    # def merge_node(self, node1, node2) -> TreeNode:
    #     if not node1:
    #         return node2
    #     if not node2:
    #         return node1
    #     if node1 and node2:
    #         return TreeNode(val=node1.val + node2.val)
