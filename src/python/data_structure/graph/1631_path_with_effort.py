"""
https://leetcode.com/problems/path-with-minimum-effort/

"""

from typing import List
import sys


# Dijkstra包含一些动态规划的思想我不是很理解
# 暂时用DFS暴力求解, 超时
class Solution:
    def __init__(self):
        # self.min_height_diff = -1
        self.result = sys.maxsize
        self.node_count = 0
        self.heights = None

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        graph = self.build_graph(heights)
        print(graph)
        self.node_count = len(graph.keys())
        self.heights = heights
        self.traverse(graph, 0, cur_path=[], cur_cost=0)
        return self.result

    def _get_height(self, node_id):
        y = node_id // len(self.heights[0])
        x = node_id % len(self.heights[0])

        return self.heights[y][x]

    def traverse(self, graph, node, cur_path, cur_cost):
        if node == self.node_count - 1:
            # print('in!!!!')
            if cur_cost < self.result:
                self.result = cur_cost
            return

        # if node in cur_path:
        #     # already on path
        #     return

        node_height = self._get_height(node)
        prev_cost = cur_cost
        for neb in graph[node]:
            if neb[0] in cur_path:
                continue
            cur_path.append(neb[0])  # 这里可以用boolean数组优化
            if abs(node_height - neb[1]) > cur_cost:
                cur_cost = abs(node_height - neb[1])
                # print('node:', node, '@', node_height, ', neb:', neb[0], '@', neb[1], ', cost:', cur_cost)
            self.traverse(graph, neb[0], cur_path, cur_cost)
            cur_path.pop()
            cur_cost = prev_cost

    def build_graph(self, heights):
        y = len(heights)
        x = len(heights[0])

        graph = {}
        node_id = 0

        def _add_neighbours(graph, node_id, i, j):
            ops = [
                (-1, 0),  # left
                (1, 0),  # right
                (0, -1),  # down
                (0, 1)  # up
            ]
            for op in ops:
                if 0 <= j + op[0] <= x - 1 and 0 <= i + op[1] <= y - 1:
                    nid = node_id + op[0] + op[1] * y
                    # (node, heights)
                    graph[node_id].append((nid, heights[i + op[1]][j + op[0]]))

        for i in range(y):
            for j in range(x):
                graph[node_id] = []
                _add_neighbours(graph, node_id, i, j)
                node_id += 1

        return graph


# heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
# heights = [[1, 10, 6, 7, 9, 10, 4, 9]]

heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
# heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
print(Solution().minimumEffortPath(heights))
