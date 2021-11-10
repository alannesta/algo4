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
        """
        reverse with the help of a stack
        :param head:
        :param left:
        :param right:
        :return:
        """
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
            # peek: increase the counter first
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

    def reverseBetween_v2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        reverse using subroutine
        :param head:
        :param left:
        :param right:
        :return:
        """
        if not head:
            return None

        if right == left:
            return head

        dummy = ListNode(val=-1, next=head)
        cnt = 0
        prev_n = next_n = reverse_head = reverse_tail = None

        start = dummy

        while start:
            cnt += 1

            if cnt == left:
                prev_n = start
                reverse_head = start.next

            elif cnt == right:
                # reverse_tail = start.next
                next_n = start.next.next if start.next else None

            start = start.next

        new_head = self.reverse(reverse_head)

        prev_n.next = new_head
        reverse_head.next = next_n

        return dummy.next

    def reverse(self, head_node) -> Optional[ListNode]:
        """
        reverse linked list (non-recursive)
        :param head_node:
        :return:
        """
        if not head_node:
            return None

        prev = cur = head_node
        cur = cur.next
        prev.next = None

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        return prev

