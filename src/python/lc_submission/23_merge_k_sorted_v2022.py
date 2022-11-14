"""
LC23: https://leetcode.com/problems/merge-k-sorted-lists/
2022 refresh
"""

from typing import List, Optional
import heapq
from collections import defaultdict, deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        res_head = ListNode()
        node_mapper = defaultdict(deque)

        for head in lists:
            if head:
                # (node val, node ref)
                heapq.heappush(min_heap, head.val)
                node_mapper[head.val].appendleft(head)

        while min_heap:
            next_val = heapq.heappop(min_heap)
            next_node = node_mapper[next_val].pop()
            res_head.next = next_node

            if next_node.next:
                heapq.heappush(min_heap, next_node.next.val)
                node_mapper[next_node.next.val].appendleft(next_node.next)

        return res_head.next
