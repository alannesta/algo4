"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:

“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

"""
from .utils import deserialize, drawtree, serialize


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
Runtime: 88 ms, faster than 42.91% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 29.6 MB, less than 5.90% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ANCESTOR_DICT = {}

        def walk(node):
            # break if p and q have both been visited
            if p.val in ANCESTOR_DICT and q.val in ANCESTOR_DICT:
                return

            if node.left:
                ANCESTOR_DICT[node.left.val] = node
                walk(node.left)

            if node.right:
                ANCESTOR_DICT[node.right.val] = node
                walk(node.right)

        walk(root)


        # find common ancester: redundant loop
        # q_parents = [q]
        #
        # v = ANCESTOR_DICT.get(q.val)
        # while v:
        #     q_parents.append(v)
        #     v = ANCESTOR_DICT.get(v.val)
        #
        # p_parents = [p]
        #
        # v = ANCESTOR_DICT.get(p.val)
        # while v:
        #     p_parents.append(v)
        #     v = ANCESTOR_DICT.get(v.val)
        #
        # for i in range(len(q_parents)):
        #     for j in range(len(p_parents)):
        #         if q_parents[i] == p_parents[j]:
        #             return q_parents[i]

        # optimized, only loop once
        q_parents = [q]

        v = ANCESTOR_DICT.get(q.val)
        while v:
            q_parents.append(v)
            v = ANCESTOR_DICT.get(v.val)

        while p:
            if p in q_parents:
                return p
            p = ANCESTOR_DICT.get(p.val)

        return None
