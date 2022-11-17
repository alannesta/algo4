"""
https://leetcode.com/problems/find-eventual-safe-states/

本质是判断以某节点开始是否有环
"""

from typing import List


# first try这个解法是正确的，但是不够高效
class Solution:
    def __init__(self):
        # record nodes that has cycle
        # self.has_cycle = {}
        self.unsafe_node = []
        self.result = []

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        cur_path = [False] * len(graph)
        visited = [False] * len(graph)
        self.unsafe_node = [False] * len(graph)

        for i in range(len(graph)):
            self.traverse(graph, i, cur_path, visited)

        for i in range(len(self.unsafe_node)):
            if self.unsafe_node[i] is False:
                self.result.append(i)

        return self.result

    def traverse(self, graph, node, cur_path, visited):
        if cur_path[node] or self.unsafe_node[node]:
            # cycle detected
            # 这一步时导致超时的主要原因
            for i in range(len(cur_path)):
                if cur_path[i] is True:
                    self.unsafe_node[i] = True
            return 1

        if visited[node]:
            return

        visited[node] = True
        cur_path[node] = True
        for connected_node in graph[node]:
            if self.traverse(graph, connected_node, cur_path, visited) == 1:
                # if 1 cycle is detected starting from node, break
                cur_path[node] = False
                break
        cur_path[node] = False


# 不超时的优化版
class Solution2:
    def __init__(self):
        self.unsafe_node = []
        self.result = []

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        cur_path = [False] * len(graph)
        visited = [False] * len(graph)
        self.unsafe_node = [False] * len(graph)

        for i in range(len(graph)):
            self.traverse(graph, i, cur_path, visited)

        for i in range(len(self.unsafe_node)):
            if self.unsafe_node[i] is False:
                self.result.append(i)

        return self.result

    def traverse(self, graph, node, cur_path, visited):
        # 主要的优化在于此, 不再重新将path上的所有node都在unsafe list里重新set一遍(O(N))
        # 这背后的逻辑其实需要进行一下证明:
        # 因为最终所有的potentially unsafe node都会在traverse时遇到另一个unsafe node, 从而被标记
        if cur_path[node]:
            # on path, cycle detected
            self.unsafe_node[node] = True
            return False

        if self.unsafe_node[node]:
            # cycle detected
            return False

        if visited[node]:
            return True

        visited[node] = True
        cur_path[node] = True
        for connected_node in graph[node]:
            if self.traverse(graph, connected_node, cur_path, visited) == False:
                # if 1 cycle is detected starting from node, terminate search for this node
                cur_path[node] = False
                self.unsafe_node[node] = True
                return False
        cur_path[node] = False

        return True
