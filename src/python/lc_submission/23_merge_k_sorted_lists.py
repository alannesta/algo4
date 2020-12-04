"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        min_heap = []

        for head_node in lists:
            heapq.heappush(min_heap, head_node)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


