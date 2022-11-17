"""
https://leetcode.com/problems/find-eventual-safe-states/

本质是判断以某节点开始是否有环
"""

from typing import List

# 2022 update: 这个写法在新加入的test case下会超时
class Solution:
    def __init__(self):
        # record nodes that has cycle
        self.has_cycle = {}
        # self.safe_node = set()

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        for node_idx, _ in enumerate(graph):
            cur_path = []
            self._traverse(graph, node_idx, cur_path)

        return sorted(set(range(len(graph))) - set(self.has_cycle.keys()))

        # return sorted(list(self.safe_node))

    def _traverse(self, graph, node, cur_path):
        if cur_path and cur_path[0] in self.has_cycle:
            return

        if node in self.has_cycle:
            for n in cur_path:
                self.has_cycle[n] = True
            return

        if node in cur_path:
            for n in cur_path:
                self.has_cycle[n] = True
            return

        cur_path.append(node)

        # traverse neighbours of node
        for neighbour in graph[node]:
            self._traverse(graph, neighbour, cur_path)

        cur_path.pop()
