"""
https://leetcode.com/problems/reverse-linked-list-ii/

Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

"""
from typing import Optional

from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        stack = deque()
        # dummy header node.
        # this makes edge case where left == 1 easier
        begin = start = ListNode()
        start.next = head
        cnt = 0

        left_ptr = None
        right_ptr = None

        while start:
            cnt = cnt + 1
            if cnt == left:
                left_ptr = start

            start = start.next

            if cnt == right:
                stack.append(start)
                right_ptr = start.next
                break

            if cnt >= left:
                stack.append(start)

        while stack:
            node = stack.pop()
            left_ptr.next = node
            left_ptr = node

        left_ptr.next = right_ptr

        return begin.next

