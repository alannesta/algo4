"""
LRU cache implemented via deque, ordered_dict, functools
"""
from collections import deque, OrderedDict
from data_structure.linked_list.double_linked_list import DELinkedList, Node


class lru:
    """
    Not an optimized implementation.
    The idea is to use a dict(hashmap) for set/get operation, and use a linked list to maintain order (lru) of keys
    """
    def __init__(self, size):
        self.size = size
        self.cache = deque()  # fresh element will be appended to head(left)
        self.cache_lookup = dict()
        # self.sentinel = object()    # unique object to identify cache miss

    def get(self, key):
        if key in self.cache_lookup:
            self.cache.remove(key)     # this is not optimized, O(N) operation
            self.cache.appendleft(key)
            return self.cache_lookup.get(key, None)

        return None

    def set(self, key, value):
        if key in self.cache_lookup:
            # O(N) operation
            self.cache.remove(key)  # remove from cache deque
            self.cache.appendleft(key)  # add to head
        else:
            if len(self.cache) >= self.size:
                # remove the least frequently used elem from right of queue
                del_key = self.cache.pop()  # O(1) operation
                del self.cache_lookup[del_key]

            self.cache.appendleft(key)

        self.cache_lookup[key] = value


class lru_final_evolution:
    """
    O(1) impl by use a Node{val, prev, next} structure(linked list node) to save value
    """

    def __init__(self, size):
        self.size = size
        self.cache = DELinkedList()  # fresh element will be appended to head(left)
        self.cache_lookup = dict()
        # self.sentinel = object()    # unique object to identify cache miss

    def get(self, key):
        if key in self.cache_lookup:
            node = self.cache_lookup.get(key)
            self.cache.remove_node(node)
            self.cache.append_left(node.val)
            return node.val[1]

        return None

    def set(self, key, value):
        if key in self.cache_lookup:
            node = self.cache_lookup.get(key)
            self.cache.remove_node(node)    # O(1) operation
            self.cache.append_left((key, value))    # (key, value) tuple passed to Node.val
        else:
            # O(1) operation
            if self.cache.size >= self.size:
                del_key = self.cache.pop_right().val[0]  # remove the least frequently used elem from right of queue
                del self.cache_lookup[del_key]

            self.cache.append_left((key, value))

        self.cache_lookup[key] = self.cache.head  # "fresh" key will always be at the head of the cache


class lru_custom_deque:
    def __init__(self, size):
        self.size = size
        self.cache = DELinkedList()  # fresh element will be appended to head(left)
        self.cache_lookup = dict()

    def get(self, key):
        if key in self.cache_lookup:
            self.cache.remove_elem(key)
            self.cache.append_left(key)
            return self.cache_lookup.get(key, None)

        return None

    def set(self, key, value):
        if key in self.cache_lookup:
            self.cache.remove_elem(key)  # remove from cache deque
            self.cache.append_left(key)  # add to head
        else:
            if self.cache.size >= self.size:
                del_key = self.cache.pop_right().val  # remove the least frequently used elem from right of queue
                del self.cache_lookup[del_key]

            self.cache.append_left(key)

        self.cache_lookup[key] = value


# OrderedDict impl
# the inside implementation of ordered dict is a linked list plus a lookup map
# Performance is similar with the deque + map impl
class lru_ordered_dict:
    def __init__(self, size):
        self.cache = OrderedDict()
        self.size = size

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)  # move to the tail
            return self.cache.get(key, None)

        return None

    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value

        else:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False)  # remove from head

            self.cache[key] = value  # "append" to "tail" of the dict
