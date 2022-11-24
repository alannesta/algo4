"""
https://leetcode.com/problems/path-with-minimum-effort/

"""

from typing import List
import heapq
import sys


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        graph = self.build_graph(heights)
        node_count = len(graph.keys())

        node_heap = []
        # init with current max diff
        visited = [sys.maxsize] * node_count
        node_cache = set()
        # (node_id, current_max_diff)
        # current_max_diff = 123
        heapq.heappush(node_heap, (0, 0))
        # node_cache.add(0)
        # print(graph)

        def _get_height(node_id):
            x = node_id // len(heights)
            y = x % len(heights)

            return heights[x][y]


        while node_heap:
            cur_node = heapq.heappop(node_heap)

            for neighbours in graph[cur_node[0]]:
                if abs(neighbours[1] - _get_height(cur_node[1])) < visited[neighbours[0]]:
                    # lower height diff than current max
                    visited[neighbours[0]] = abs(neighbours[1] - cur_node[1])
                    heapq.heappush(node_heap, neighbours)
                else:
                    # there is a path with lower diff to this node
                    continue

        # last node
        return visited[-1]

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
                if 0 <= i + op[0] <= y - 1 and 0 <= j + op[1] <= y - 1:
                    nid = node_id + op[1] + op[0] * y
                    # (node, heights)
                    graph[node_id].append((nid, heights[i + op[0]][j + op[1]]))

        for i in range(y):
            for j in range(x):
                graph[node_id] = []
                _add_neighbours(graph, node_id, i, j)
                node_id += 1

        return graph


heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]

Solution().minimumEffortPath(heights)
