"""
743. Network Delay Time
"""

from typing import List

# 求出的解是正确的，但是会超时
class Solution:
    def __init__(self):
        self.visited = []
        self.time_cost = []

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self.build_graph(times, n)
        self.visited = [(False, 0)] * n  # index need to an offset
        cur_path = [False] * n  # index need to an offset
        self.traverse(graph, k, cur_path, 0)

        max_cost = 0
        print(self.visited)
        for is_visited, cost in self.visited:
            if is_visited is False:
                return -1
            else:
                if cost > max_cost:
                    max_cost = cost

        return max_cost

    def traverse(self, graph, node, cur_path, cur_cost):
        # record cost
        if self.visited[node - 1][0] is True:
            if cur_cost < self.visited[node - 1][1]:
                self.visited[node - 1] = (True, cur_cost)
        else:
            self.visited[node - 1] = (True, cur_cost)

        if cur_path[node - 1]:
            # cycle
            return

        cur_path[node - 1] = True
        for edge in graph[node]:
            self.traverse(graph, edge[0], cur_path, cur_cost + edge[1])
        cur_path[node - 1] = False

    def build_graph(self, times, node_count):
        graph = {}
        for i in range(1, node_count + 1):
            graph[i] = []

        for edge in times:
            # source : (target, cost)
            graph[edge[0]].append((edge[1], edge[2]))

        return graph

