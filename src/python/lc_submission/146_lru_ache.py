"""
https://leetcode.com/problems/lru-cache/
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = DELinkedList()  # fresh element will be appended to head(left)
        self.cache_lookup = dict()

    def get(self, key: int) -> int:
        print('before get: \t\t{}'.format(self.cache))
        # if self.cache.size > 10:
        #     raise Exception('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!OVERRRRRRR SIZE: ')
        print('get {}'.format(key))
        if key in self.cache_lookup:
            node = self.cache_lookup.get(key)
            self.cache.remove_node(node)
            self.cache.append_left(node.val)
            print('return {}'.format(node.val[1]))
            print('after  get: \t\t{}'.format(self.cache))
            self.cache_lookup[key] = self.cache.head
            return node.val[1]

        return -1

    def put(self, key: int, value: int) -> None:
        print('before put: \t\t{}'.format(self.cache))
        print('put {} : {}'.format(key, value))
        if key == 9:
            print('current look up dict:', self.cache_lookup.keys())
        if key in self.cache_lookup:
            node = self.cache_lookup.get(key)
            self.cache.remove_node(node)
            self.cache.append_left((key, value))
        else:
            if self.cache.size == self.size:
                del_key = self.cache.pop_right().val[0]
                try:
                    del self.cache_lookup[del_key]
                except KeyError:
                    print('cannot find key: ', del_key)
                    raise

            self.cache.append_left((key, value))

        self.cache_lookup[key] = self.cache.head
        print('after  put: \t\t{}'.format(self.cache))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


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

        node = None
        self.size -= 1

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


ops = ["LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
       "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
       "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
       "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
       "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
       "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
       "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]

input = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
         [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11],
         [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5],
         [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22],
         [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29],
         [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27],
         [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7],
         [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

expected_output = [None, None, None, None, None, None, -1, None, 19, 17, None, -1, None, None, None, -1, None, -1, 5,
                   -1, 12, None, None, 3, 5, 5, None, None, 1, None, -1, None, 30, 5, 30, None, None, None, -1, None,
                   -1, 24, None, None, 18, None, None, None, None, -1, None, None, 18, None, None, -1, None, None, None,
                   None, None, 18, None, None, -1, None, 4, 29, 30, None, 12, -1, None, None, None, None, 29, None,
                   None, None, None, 17, 22, 18, None, None, None, -1, None, None, None, 20, None, None, None, -1, 18,
                   18, None, None, None, None, 20, None, None, None, None, None, None, None]
ops.pop(0)
input.pop(0)
expected_output.pop(0)

cache = LRUCache(10)
output = []
i = 0
for operation in zip(ops, input):
    if i == 19:
        print('ss')
    # print(operation)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('operation: {}'.format(i))
    method = getattr(cache, operation[0])
    ret = method(*operation[1])
    if operation[0] == 'get':
        print('expected output {}'.format(expected_output[i]))
        if expected_output[i] != ret:
            raise Exception('Error in output')
    output.append(ret)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    i += 1

# print(list(zip(ops, input))[43])

# print(expected_output)
# print(output)
