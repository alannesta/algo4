"""
https://leetcode.com/problems/min-stack/
"""

from collections import defaultdict
import heapq


# "暴力"解法, 累死电脑不累脑子
# heap with tombstone
class MinStack:

    def __init__(self):
        self.main_stack = []
        self._min_heap = []
        self.min = 2 ** 31 - 1

    def push(self, val: int) -> None:
        record = [val, True]
        self.main_stack.append(record)
        heapq.heappush(self._min_heap, record)

    def pop(self) -> None:
        removed = self.main_stack.pop()
        if removed == self._min_heap[0]:
            heapq.heappop(self._min_heap)
        else:
            # tomb stone
            removed[1] = False

    def top(self) -> int:
        return self.main_stack[-1][0]

    def getMin(self) -> int:
        while True:
            if self._min_heap[0][1] == False:
                self._min_heap.pop()
            else:
                break
        return self._min_heap[0][0]


# 辅助stack的解法, 需要一些思考
class MinStack2:
    def __init__(self):
        self.main_stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self) -> None:
        removed = self.main_stack.pop()
        if removed == self._min_stack[-1]:
            self._min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]


# linked list + 节点辅助数据, 我最喜欢的一个解法, 也是submission里最快的一个解法
class MinStack3:
    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if not self.head:
            self.head = Node(val, cur_min=val)
        else:
            prev = self.head
            self.head = Node(val, cur_min=min(prev.cur_min, val), next=prev)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.cur_min


class Node:
    def __init__(self, val, cur_min, prev=None, next=None):
        self.val = val
        self.cur_min = cur_min
        self.prev = prev
        self.next = next
