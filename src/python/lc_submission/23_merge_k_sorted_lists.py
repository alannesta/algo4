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


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        start = head = ListNode()

        head_queue = []
        node_mapper = {}

        # init
        for h_node in lists:
            if h_node:
                heapq.heappush(head_queue, h_node.val)
                if not node_mapper[h_node.val]:
                    node_mapper[h_node.val] = [h_node]
                else:
                    node_mapper[h_node.val].append(h_node)

        while True:
            if not head_queue:
                break

            smallest = heapq.heappop(head_queue)
            node = node_mapper[smallest].pop()

            head.next = node
            head = node

            if node.next:
                heapq.heappush(head_queue, node.next.val)
                if not node_mapper[node.next.val]:
                    node_mapper[node.next.val] = [node.next]
                else:
                    node_mapper[node.next.val].append(node.next)


        return start.next