"""
https://leetcode.com/problems/serialize-and-deserialize-bst/

Design an algorithm to serialize and deserialize a binary search tree.

There is no restriction on how your serialization/deserialization algorithm should work.

You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.
"""

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.str_repr = ''

    def serialize(self, root: TreeNode) -> str:
        """
        using pre-order traversal
        """
        self.traverse(root)
        return self.str_repr

    def traverse(self, node):
        if not node:
            self.str_repr += 'null,'
            return

        self.str_repr += f'{str(node.val)},'

        self.traverse(node.left)
        self.traverse(node.right)

    def deserialize(self, data: str) -> TreeNode:
        """
        deserialize, O(N)
        """

        data = data.split(',')
        data.pop()  # remove the last elem (extra comma)

        root = self.construct(deque(data))

        return root

    def construct(self, data: deque[str]) -> Optional[TreeNode]:
        if not data:
            return None

        head = data.popleft()  # pop the first elem

        if head == 'null':
            return None
        else:
            node = TreeNode(int(head))

            node.left = self.construct(data)
            node.right = self.construct(data)

            return node

    def serialize_v2(self, root: TreeNode) -> str:
        """
        BFS, level-order traversal
        """
        queue = deque()
        queue.appendleft(root)

        while queue:
            node = queue.pop()

            if node:
                self.str_repr += f'{str(node.val)},'
                queue.appendleft(node.left)
                queue.appendleft(node.right)
            else:
                # node is null
                self.str_repr += '#,'

        return self.str_repr

    def deserialize_v2(self, data: str) -> Optional[TreeNode]:
        """
        deserialize, level-order traversal, O(N)
        """

        data = data.split(',')
        data.pop()  # remove the last elem (extra comma)
        data.reverse()  # reverse to pop

        elem = data.pop()
        node_queue = deque()

        if elem == '#':
            return None
        else:
            root = TreeNode(int(elem))
            node_queue.appendleft(root)

        while data:
            node = node_queue.pop()

            left = data.pop()

            if left == '#':
                node.left = None
            else:
                left_n = TreeNode(int(left))
                node.left = left_n
                node_queue.appendleft(left_n)

            right = data.pop()

            if right == '#':
                node.right = None
            else:
                right_n = TreeNode(int(right))
                node.right = right_n
                node_queue.appendleft(right_n)

        return root
