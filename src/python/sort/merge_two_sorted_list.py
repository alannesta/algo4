"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = node_ptr = ListNode()
        ptr1 = l1
        ptr2 = l2

        while ptr1 is not None and ptr2 is not None:
            while ptr1 is not None and ptr1.val <= ptr2.val:
                node_ptr.next = ListNode(ptr1.val)
                node_ptr = node_ptr.next
                ptr1 = ptr1.next

            if ptr1 is None:
                break

            while ptr2 is not None and ptr2.val < ptr1.val:
                node_ptr.next = ListNode(ptr2.val)
                node_ptr = node_ptr.next
                ptr2 = ptr2.next

        if ptr1 is None:
            node_ptr.next = ptr2
            return head.next

        if ptr2 is None:
            node_ptr.next = ptr1
            return head.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(4)
n1.next = n2
n2.next = n3

n4 = ListNode(1)
n5 = ListNode(3)
n6 = ListNode(4)

n4.next = n5
n5.next = n6

sol = Solution()
res = sol.mergeTwoLists(n1, n4)
# print(res)
while res:
    print(res.val)
    res = res.next