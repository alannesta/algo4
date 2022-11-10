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

from collections import deque, defaultdict


# LFU 2022 refresh
class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cur_elem = 0
        self.min_freq = 0
        self.cache = {}
        self.freq_tracker = defaultdict(deque)

    def put(self, key, val):
        if self.capacity == 0:
            return
        if key in self.cache:
            node = self.cache[key]
            node[0] = val
            self.freq_tracker[node[1]].remove(key)
            self.freq_tracker[node[1] + 1].appendleft(key)
            if not self.freq_tracker[node[1]] and self.min_freq == node[1]:
                self.min_freq = node[1] + 1
            node[1] += 1
        else:
            if self.cur_elem < self.capacity:
                self.cur_elem += 1
            else:
                # evict
                key_to_evict = self.freq_tracker[self.min_freq].pop()
                del self.cache[key_to_evict]

            self.cache[key] = [val, 1]
            self.freq_tracker[1].appendleft(key)
            self.min_freq = 1

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.freq_tracker[node[1]].remove(key)
        self.freq_tracker[node[1] + 1].appendleft(key)
        if not self.freq_tracker[node[1]] and self.min_freq == node[1]:
            self.min_freq = node[1] + 1
        # modify node freq
        node[1] += 1
        return node[0]
