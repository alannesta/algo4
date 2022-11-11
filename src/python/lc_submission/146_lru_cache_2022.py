"""
2022 refresh
经典题目, 一年一刷
"""


class CacheNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_size = 0
        self.cache = {}
        self.node_list_head = CacheNode(None, None, None, None)
        self.node_list_tail = CacheNode(None, None, None, None)

        # link
        self.node_list_tail.prev = self.node_list_head
        self.node_list_head.next = self.node_list_tail

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # move cache node towards head
        self._move_node_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            # move cache node towards head
            self._move_node_to_head(node)

        else:
            new_node = CacheNode(key, value)
            self.cache[key] = new_node
            if self.cache_size == self.capacity:
                # add and evict
                node_to_evict = self.node_list_tail.prev  # this should not be head, if capacity is not 0
                evict_prev = node_to_evict.prev
                evict_prev.next = self.node_list_tail
                self.node_list_tail.prev = evict_prev
                del self.cache[node_to_evict.key]
            else:
                self.cache_size += 1

            head_tmp = self.node_list_head.next
            self.node_list_head.next = new_node
            new_node.next = head_tmp
            new_node.prev = self.node_list_head
            head_tmp.prev = new_node

    def _move_node_to_head(self, node):
        head_tmp = self.node_list_head.next

        if head_tmp == node:
            return

        node_tmp_prev = node.prev
        node_tmp_next = node.next

        self.node_list_head.next = node
        node.next = head_tmp
        node.prev = self.node_list_head
        head_tmp.prev = node

        node_tmp_prev.next = node_tmp_next
        node_tmp_next.prev = node_tmp_prev


# 使用OrderedDict, 直接大结局
# 不需要在自己manage linked list, OrderedDict帮你搞定
from collections import OrderedDict

class LRUCacheV2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_size = 0
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        val = self.cache[key]
        # move cache node towards end
        self.cache.move_to_end(key, last=True)
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            # update cache
            self.cache[key] = value
            # move node to end of list
            self.cache.move_to_end(key, last=True)
            return

        # add to cache
        # new node are added to the end of internal list
        self.cache[key] = value

        if self.cache_size < self.capacity:
            self.cache_size += 1
        else:
            # evict from head
            # 这个api挺confusing的
            self.cache.popitem(last=False)