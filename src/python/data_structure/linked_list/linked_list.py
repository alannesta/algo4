"""
Linked list impl
"""
import copy


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self, val):
        a_node = Node(val=val)
        if not self._is_empty():
            self.tail.next = a_node
            self.tail = a_node
        else:
            self.head = self.tail = a_node

    def add_first(self, val):
        a_node = Node(val=val)

        if not self._is_empty():
            a_node.next = self.head
            self.head = a_node
        else:
            self.head = self.tail = a_node

    def add(self, idx, val):
        i_node = Node(val=val)
        if idx == 0:
            self.add_first(i_node)
        else:
            ptr = self.head
            insert_node = None
            cursor = 1
            while ptr:
                if cursor == idx:
                    insert_node = ptr
                    break
                cursor += 1
                ptr = ptr.next

            # found the insertion node
            if insert_node:
                temp = insert_node.next
                insert_node.next = i_node
                if temp:
                    i_node.next = temp
            else:
                raise IndexError('index {} out of range'.format(idx))

    def get(self, idx):
        cursor = 0
        ptr = self.head
        while ptr:
            if cursor == idx:
                return ptr.val
            cursor += 1
            ptr = ptr.next

        raise IndexError('index {} out of range'.format(idx))

    def remove(self, idx):
        prev_node = None
        cur_node = self.head
        cursor = 0
        while cur_node:
            if cursor == idx:
                if prev_node:
                    prev_node.next = cur_node.next
                    return
                else:
                    # idx is 0
                    self.head = cur_node.next
                    return
            cursor += 1
            prev_node = cur_node
            cur_node = cur_node.next

        raise IndexError('index {} out of range'.format(idx))

    def _is_empty(self):
        return self.head is None or self.tail is None

    def __str__(self):
        if self.head is None:
            return 'list is emtpy'
        else:
            result = ''
            ptr = self.head
            while ptr:
                result += str(ptr.val) + '-->'
                ptr = ptr.next

            return result


class Node:
    def __init__(self, val=None, next=None):
        if next:
            assert isinstance(next, Node)
        self.next = next
        self.val = val
