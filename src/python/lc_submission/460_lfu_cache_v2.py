"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.

When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item.
For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency),
the least recently used key would be evicted.

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

from collections import deque


class CacheNode:
    def __init__(self, key, val, freq, prev=None, next=None):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f'[{self.key}: {self.val}]'


class LinkedList:
    """
    double linked list which supports add/remove nodes from both ends
    """

    def __init__(self):
        self.head = CacheNode(key=None, val=None, freq=None)
        self.tail = CacheNode(key=None, val=None, freq=None, prev=self.head)

        self.head.next = self.tail
        self.size = 0

    def appendleft(self, node: CacheNode):
        cur_head = self.head.next

        self.head.next = node
        cur_head.prev = node

        node.prev = self.head
        node.next = cur_head

        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError

        cur_tail = self.tail.prev
        cur_tail_prev = cur_tail.prev

        cur_tail_prev.next = self.tail
        self.tail.prev = cur_tail_prev

        # cur_tail.prev = None
        # cur_tail.next = None

        self.size -= 1

        return cur_tail


    def remove(self, node: CacheNode):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.size -= 1


    def __len__(self):
        return self.size


class LFUCache:

    def __init__(self, capacity: int):
        self.cache_lookup = {}
        self.freq_lookup = {
            0: LinkedList()
        }
        self.current_cap = 0
        self.capacity = capacity
        self.lowest_freq = 0  # starting value, need caution

    def get(self, key: int) -> int:
        cache_node = self.cache_lookup.get(key, None)
        if cache_node:
            # update freq
            cur_freq = cache_node.freq

            # update key, update freq
            cache_node.freq = cur_freq + 1

            self.freq_lookup[cur_freq].remove(cache_node)  # deque remove api
            self._add_to_freq_map(cache_node)

            # update lowest_freq pointer
            if len(self.freq_lookup[self.lowest_freq]) == 0:
                self.lowest_freq = self.lowest_freq + 1

            return cache_node.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        cache_node = self.cache_lookup.get(key, None)

        if cache_node:
            cur_freq = cache_node.freq
            self.freq_lookup[cur_freq].remove(cache_node)  # deque remove api

            # update key, update freq
            cache_node.freq = cur_freq + 1
            cache_node.val = value

            self._add_to_freq_map(cache_node)

            # update low freq pointer
            if len(self.freq_lookup[self.lowest_freq]) == 0 or self.lowest_freq == 0:
                self.lowest_freq = cur_freq + 1

        else:
            new_node = CacheNode(key=key, val=value, freq=1)

            if self.current_cap < self.capacity:
                # add key

                self.cache_lookup[key] = new_node
                self._add_to_freq_map(new_node)

                self.lowest_freq = 1

                self.current_cap += 1

            else:
                # remove key with least freq
                try:
                    node_to_remove = self.freq_lookup[self.lowest_freq].pop()
                except IndexError:
                    return
                self.cache_lookup.pop(node_to_remove.key)

                # add key
                self.cache_lookup[key] = new_node
                self._add_to_freq_map(new_node)

                self.lowest_freq = 1

    def _add_to_freq_map(self, cache_node):
        if cache_node.freq in self.freq_lookup:
            self.freq_lookup[cache_node.freq].appendleft(cache_node)
        else:
            self.freq_lookup[cache_node.freq] = LinkedList()
            self.freq_lookup[cache_node.freq].appendleft(cache_node)

# lfu = LFUCache(2)
# lfu.put(3, 1)
# lfu.put(2, 2)
# lfu.put(2, 1)
# lfu.put(4, 4)
#
# print(lfu.get(2))
