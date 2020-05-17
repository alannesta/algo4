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


class LFU:
    def __init__(self, size):
        self.size = size
        self.freq_queue = deque()
        self.cache_lookup = dict()

    def get(self, key):
        if key in self.cache_lookup:
            freq, lookup_key, value = self.cache_lookup.get(key)
            self.freq_queue.remove((freq, lookup_key, value))
            updated_freq = freq + 1

            self._update_cache((updated_freq, lookup_key, value))

            return value

        return -1

    def put(self, key, value):
        if self.size == 0:
            return

        if key in self.cache_lookup:
            freq, lookup_key, old_val = self.cache_lookup.get(key)
            self.freq_queue.remove((freq, lookup_key, old_val))

            self._update_cache((freq + 1, lookup_key, value))
        else:
            if len(self.cache_lookup.keys()) == self.size:
                if len(self.cache_lookup) > 0:
                    _, evict_key, _ = self.freq_queue.popleft()
                    del self.cache_lookup[evict_key]
            self._update_cache((1, key, value))

    def _update_cache(self, tup):
        updated_freq, lookup_key, value = tup
        if len(self.freq_queue) == 0:
            self.cache_lookup[lookup_key] = tup
            return self.freq_queue.append(tup)

        insert_idx = len(self.freq_queue) - 1
        while self.freq_queue[insert_idx][0] > updated_freq and insert_idx >= 0:
            insert_idx -= 1

        self.freq_queue.insert(insert_idx + 1, (updated_freq, lookup_key, value))
        self.cache_lookup[lookup_key] = tup


# cache = LFU(size=3)
#
# cache.put(1, 1)
# cache.put(2, 2)
# cache.get(1)  # returns 1
# cache.put(3, 3)  # evicts key 2
# cache.get(2)  # returns -1 (not found)
# cache.get(3)  # returns 3.
# cache.put(4, 4)  # evicts key 1.
#
# cache.get(4)  # returns 4
