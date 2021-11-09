"""
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome.


这是很经典的一道面试题目. O(1)空间开销的solution涉及到了快慢指针寻找中间节点. 反转链表等求解链表问题的的常见技巧
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        O(1) space complexity, O(N) time complexity
        :param head:
        :return:
        """
        ptr1 = ptr2 = head

        while ptr1 and ptr1.next:
            ptr1 = ptr1.next.next
            ptr2 = ptr2.next

        if ptr1 and not ptr1.next:
            ptr2 = ptr2.next  # move one more step if linked list has odd number of nodes

        head2 = self.reverse(ptr2)

        while head2:
            # need to compare val, not reference of node
            if head.val != head2.val:
                return False

            head = head.next
            head2 = head2.next

        return True

    def reverse(self, head_node) -> Optional[ListNode]:
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

    def isPalindrome_v2(self, head: Optional[ListNode]) -> bool:
        """
        using stack, O(N) space complexity, O(N) time complexity
        :param head:
        :return:
        """
        stack = []
        ptr = head
        ptr2 = head

        while ptr:
            stack.append(ptr)
            ptr = ptr.next

        count = len(stack)

        while len(stack) > count // 2:
            node = stack.pop()

            if node.val == ptr2.val:
                ptr2 = ptr2.next
            else:
                return False

        return True
