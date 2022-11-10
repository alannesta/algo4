"""
https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key): Return the value of the key if the key exists, otherwise return -1.

void put(int key, int value): Update the value of the key if the key exists.

Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""

from typing import Optional

"""
Runtime: 892 ms, faster than 68.85% of Python3 online submissions for LRU Cache.
Memory Usage: 75.9 MB, less than 60.51% of Python3 online submissions for LRU Cache.
"""

class CacheNode:
    def __init__(self, val: Optional[int], key: Optional[int], prev, next):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

    def __repr__(self):
        return str(self.key) + " : " + str(self.val)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_cap = 0

        self.cache = {}

        # double linked list
        self.head = CacheNode(None, None, None, None)
        self.tail = CacheNode(None, None, self.head, None)

        self.head.next = self.tail

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if node:
            self._refresh_node(node)
            return node.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)

        if node:
            node.val = value
            self._refresh_node(node)

        else:
            new_node = CacheNode(value, key, None, None)
            self.cache[key] = new_node

            # if not full, insert to head
            if self.current_cap < self.capacity:
                self._insert_to_head(new_node)
                self.current_cap += 1

            # remove tail, insert to head
            else:
                to_remove = self.tail.prev
                print('remove: ', to_remove)

                self.cache.pop(to_remove.key)

                # remove last node (least frequently used)
                second_last = self.tail.prev.prev
                second_last.next = self.tail
                self.tail.prev = second_last

                # insert to head
                self._insert_to_head(new_node)

    def _refresh_node(self, node: CacheNode):
        """
        move node to head of the list
        :param node:
        :return:
        """
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        cur_head = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = cur_head
        cur_head.prev = node

    def _insert_to_head(self, node: CacheNode):
        cur_head = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = cur_head
        cur_head.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
