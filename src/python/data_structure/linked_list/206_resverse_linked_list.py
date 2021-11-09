"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

https://leetcode.com/problems/reverse-linked-list/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur = head
        cur_next = head.next
        cur.next = None

        while cur_next:
            next_node = cur_next.next
            cur_next.next = cur

            cur = cur_next
            cur_next = next_node

        return cur

    def reverse_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        recursively reverse linked list
        :param head:
        :return:
        """
        if not head:
            return None

        if head.next:
            n_head = self.reverse_recursive(head.next)

            head.next.next = head

            head.next = None

            return n_head
        else:
            return head

