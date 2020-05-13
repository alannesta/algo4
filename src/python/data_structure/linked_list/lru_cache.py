"""
LRU cache implemented via deque, ordered_dict, functools
"""
from collections import deque, OrderedDict
from data_structure.linked_list.double_linked_list import DELinkedList
from functools import lru_cache

class lru:
    def __init__(self, size):
        self.size = size
        self.cache = deque()    # fresh element will be appended to head(left)
        self.cache_lookup = dict()

    def get(self, key):
        if key in self.cache_lookup:
            self.cache.remove(key)
            self.cache.appendleft(key)
        return self.cache_lookup.get(key, None)

    def set(self, key, value):
        if key in self.cache_lookup:
            self.cache.remove(key)  # remove from cache deque
            self.cache.appendleft(key)  # add to head
        else:
            if len(self.cache) >= self.size:
                del_key = self.cache.pop()    # remove the least frequently used elem from right of queue
                del self.cache_lookup[del_key]

            self.cache.appendleft(key)

        self.cache_lookup[key] = value


class lru_custom_deque:
    def __init__(self, size):
        self.size = size
        self.cache = DELinkedList()    # fresh element will be appended to head(left)
        self.cache_lookup = dict()

    def get(self, key):
        if key in self.cache_lookup:
            self.cache.remove_elem(key)
            self.cache.append_left(key)
        return self.cache_lookup.get(key, None)

    def set(self, key, value):
        if key in self.cache_lookup:
            self.cache.remove_elem(key)  # remove from cache deque
            self.cache.append_left(key)  # add to head
        else:
            if self.cache.size >= self.size:
                del_key = self.cache.pop_right().val    # remove the least frequently used elem from right of queue
                del self.cache_lookup[del_key]

            self.cache.append_left(key)

        self.cache_lookup[key] = value

# OrderedDict impl
class lru_ordered_dict:
    def __init__(self, size):
        self.cache = OrderedDict()
        self.size = size

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)    # move to the tail
        return self.cache.get(key, None)

    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value

        else:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False)  # remove from head

            self.cache[key] = value # "append" to "tail" of the dict
