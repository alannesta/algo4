"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.


"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(val=-1, next=head)
        counter = 0  # start with 0
        prev = ptr1 = ptr2 = dummy

        # peek ptr1.next, do not incr counter if ptr1 has reached end of list
        while ptr1.next:
            ptr1 = ptr1.next

            counter = counter + 1
            # when to move ptr2? avoid off by one error by drawing on paper
            if counter >= n:
                prev = ptr2
                ptr2 = ptr2.next

        prev.next = prev.next.next

        return dummy.next
