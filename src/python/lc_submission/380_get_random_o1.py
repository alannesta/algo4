"""
https://leetcode.com/problems/insert-delete-getrandom-o1/

implement the functions of the class such that each function works in average O(1) time complexity.
"""

# from typing import Optional
import random


class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class RandomizedSet:

    def __init__(self):
        self.head = Node(val=None)
        self.tail = Node(val=None, prev=self.head)

        self.node_lookup = {}

    def insert(self, val: int) -> bool:
        if val in self.node_lookup:
            return False

        n_node = Node(val)

        prev_n = self.tail.prev
        self.tail.prev = n_node
        prev_n.next = n_node

        n_node.prev = prev_n
        n_node.next = self.tail

        self.node_lookup[val] = n_node

        return True

    def remove(self, val: int) -> bool:
        if val in self.node_lookup:
            node = self.node_lookup[val]
            prev_n = node.prev
            next_n = node.next

            prev_n.next = next_n
            next_n.prev = prev_n

            self.node_lookup.pop(val)

            return True

        return False

    def getRandom(self) -> int:
        vals = list(self.node_lookup.keys())

        return vals[random.randint(0, len(vals) - 1)]
