"""
https://leetcode.com/problems/find-duplicate-subtrees/

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Runtime: 1044 ms, faster than 5.08% of Python3 online submissions for Find Duplicate Subtrees.
Memory Usage: 28.6 MB, less than 11.00% of Python3 online submissions for Find Duplicate Subtrees.

serialization的方法耗时较多, 不知道能否优化
"""
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        memo = {}
        output = []

        def serialize(node) -> str:
            if node is None:
                return 'null'
            return str(node.val) + ',' + serialize(node.left) + ',' + serialize(node.right)

        def walk(node):
            if node is None:
                return

            key = serialize(node)
            if key in memo:
                if memo[key] == 1:
                    output.append(node)
                memo[key] = memo[key] + 1
            else:
                memo[key] = 1

            walk(node.left)
            walk(node.right)


        walk(root)

        return output