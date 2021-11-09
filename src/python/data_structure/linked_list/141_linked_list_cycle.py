"""
https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return None

        s_ptr = head
        f_ptr = head

        while f_ptr:

            f_ptr = f_ptr.next

            if not f_ptr:
                # no cycle
                return False

            f_ptr = f_ptr.next

            s_ptr = s_ptr.next

            if f_ptr == s_ptr:
                return True

        return False
