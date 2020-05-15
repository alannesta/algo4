"""
double linked list aka deque impl
"""


class DELinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append_right(self, val):
        if self.size > 0:
            node = Node(val=val, prev=self.tail)
            self.tail.next = node
            self.tail = node
        else:
            node = Node(val=val)
            self.head = self.tail = node

        self.size += 1

    def append_left(self, val):
        if self.size > 0:
            node = Node(val=val, next=self.head)
            self.head.prev = node
            self.head = node
        else:
            node = Node(val=val)
            self.head = self.tail = node

        self.size += 1

    def pop_left(self):
        if self.size == 0:
            return None

        poped = self.head
        next_head = self.head.next
        if next_head:
            next_head.prev = None
            self.head = next_head
        else:
            self.head = self.tail = None
        self.size -= 1
        return poped

    def pop_right(self):
        if self.size == 0:
            return None

        poped = self.tail
        next_tail = self.tail.prev
        if next_tail:
            next_tail.next = None
            self.tail = next_tail
        else:
            self.head = self.tail = None
        self.size -= 1
        return poped

    def add(self, idx, val):
        if self.size == 0:
            return self.append_left(val)

        if idx > self.size - 1 or idx < 0:
            raise IndexError('index: {} out of range'.format(idx))

        mid = self.size >> 1

        if idx <= mid:
            ptr = self.head
            # start from head
            while idx > 0:
                ptr = ptr.next
                idx -= 1

            prev_node = ptr.prev
            node = Node(val=val, prev=prev_node, next=ptr)
            ptr.prev = node

            if prev_node:
                prev_node.next = node
            else:
                # no more previous node, set head to node
                self.head = node
        else:
            # start from tail
            ptr = self.tail
            step = self.size - 1 - idx
            while step > 0:
                ptr = ptr.prev
                step -= 1

            next_node = ptr.next
            node = Node(val=val, prev=ptr, next=next_node)
            ptr.next = node

            if next_node:
                next_node.prev = node
            else:
                # no more next node, set tail to node
                self.tail = node

        self.size += 1

    def get(self, idx):
        if idx > self.size - 1 or idx < 0:
            raise IndexError('index: {} out of range'.format(idx))

        mid = self.size >> 1
        if idx <= mid:
            ptr = self.head
            # start from head
            while idx > 0:
                ptr = ptr.next
                idx -= 1
            return ptr.val
        else:
            ptr = self.tail
            step = self.size - 1 - idx
            while step > 0:
                ptr = ptr.prev
                step -= 1
            return ptr.val

    def remove(self, idx):
        if idx > self.size - 1 or idx < 0:
            raise IndexError('index: {} out of range'.format(idx))

        mid = self.size >> 1

        if idx <= mid:
            ptr = self.head
            # start from head
            while idx > 0:
                ptr = ptr.next
                idx -= 1

            prev_node = ptr.prev  # could be None
            next_node = ptr.next

            if prev_node:
                prev_node.next = next_node
                next_node.prev = prev_node
            else:
                # no more previous node, set head to node
                self.head = next_node
                next_node.prev = None
        else:
            # start from tail
            ptr = self.tail
            step = self.size - 1 - idx
            while step > 0:
                ptr = ptr.prev
                step -= 1

            next_node = ptr.next  # could be None
            prev_node = ptr.prev

            if next_node:
                next_node.prev = prev_node
                prev_node.next = next_node
            else:
                # no more next node, set tail to node
                self.tail = prev_node
                prev_node.next = None

        self.size -= 1

    def remove_elem(self, elem):
        """
        remove the first occurrence of an elem
        :param elem: elem to remove
        :return: None
        """
        ptr = self.head
        while ptr:
            if ptr.val == elem:
                next_node = ptr.next
                prev_node = ptr.prev

                if prev_node:
                    prev_node.next = next_node
                else:
                    self.head = next_node

                if next_node:
                    next_node.prev = prev_node
                else:
                    self.tail = prev_node

                self.size -= 1

                return

            ptr = ptr.next

        print('element {} not found in the list'.format(elem))

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        if prev_node:
            prev_node.next = next_node
        else:
            if next_node:
                self.head = next_node
            else:
                self.head = self.tail = None

        if next_node:
            next_node.prev = prev_node
        else:
            if prev_node:
                self.tail = prev_node
            else:
                self.head = self.tail = None

        self.size -= 1

    def _is_empty(self):
        return self.head is None or self.tail is None

    def __str__(self):
        if self.head is None:
            return 'list is emtpy'
        else:
            result = ''
            ptr = self.head
            while ptr:
                result += str(ptr.val) + '==='
                ptr = ptr.next

            return result


class Node:
    def __init__(self, val=None, prev=None, next=None):
        if next:
            assert isinstance(next, Node)
        if prev:
            assert isinstance(prev, Node)

        self.next = next
        self.prev = prev
        self.val = val