"""
Solution for 112 and 113
https://leetcode.com/problems/path-sum/
https://leetcode.com/problems/path-sum-ii/

"""
from typing import Optional, List
import copy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.target_sum = 0
        self.result = []
        self.found = False

    # solution for 112
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.target_sum = targetSum
        return self.traverse(root, 0)

    # solution for 113
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.target_sum = targetSum
        self.traverse113(root, cur_sum=0, cur_path=[])

    def traverse(self, node, cur_sum):
        if node is None:
            return False

        if self.found:
            return True

        cur_sum = cur_sum + node.val

        if cur_sum == self.target_sum:
            if node.left is None and node.right is None:
                self.found = True
                return True

        found_l = self.traverse(node.left, cur_sum)
        found_r = self.traverse(node.right, cur_sum)

        return found_r or found_l

    def traverse113(self, node, cur_sum, cur_path):
        if node is None:
            return

        cur_sum = cur_sum + node.val

        if cur_sum == self.target_sum:
            if node.left is None and node.right is None:
                cur_path.append(node.val)
                self.result.append(copy.copy(cur_path))
                cur_path.pop()
                return

        cur_path.append(node.val)
        self.traverse113(node.left, cur_sum, cur_path)
        self.traverse113(node.right, cur_sum, cur_path)
        cur_path.pop()
        return
