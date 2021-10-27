"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

"""


# Definition for a Node.

class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


"""
Runtime: 64 ms, faster than 72.77% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 15.6 MB, less than 92.33% of Python3 online submissions for Populating Next Right Pointers in Each Node.

"""
class Solution:
    def connect(self, root):
        if root == None:
            return
        if root.left and root.right:
            root.left.next = root.right

            if root.next:
                root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root
