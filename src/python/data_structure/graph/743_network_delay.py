"""
743. Network Delay Time
https://leetcode.com/problems/network-delay-time/
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
                # cost is already greater, no need to proceed
                return
        else:
            # not visited yet
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


import heapq


# DIJKSTRA 达基萨斯将军泉下有知
class Solution_DJ:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self.build_graph(times, n)
        # 这里可以简化, 只使用一维数组来做记录, index就是node的number
        # 初始化时将cost初始化为一个足够大的值, 比如sys.maxsize
        visited = [[False, 0]] * n  # index need to an offset

        min_heap = []

        # (cost, node)
        heapq.heappush(min_heap, (0, k))
        visited[k - 1] = [True, 0]

        while min_heap:
            # cur_node (cost, node)
            # neighbour (node, cost)
            # visited [(bool, cost)...]
            cur_node = heapq.heappop(min_heap)
            for neighbour in graph[cur_node[1]]:
                if not visited[neighbour[0] - 1][0]:
                    # first visit
                    # record cost = cur_node cost + edge cost
                    visited[neighbour[0] - 1] = [True, cur_node[0] + neighbour[1]]
                    heapq.heappush(min_heap, (cur_node[0] + neighbour[1], neighbour[0]))
                else:
                    # already visited
                    # if cost is lower, update cost
                    if cur_node[0] + neighbour[1] < visited[neighbour[0] - 1][1]:
                        visited[neighbour[0] - 1][1] = cur_node[0] + neighbour[1]
                        heapq.heappush(min_heap, (cur_node[0] + neighbour[1], neighbour[0]))
                    else:
                        # already visited, and cur cost is higher
                        # in this case, this path should not be chosen
                        continue

        max_cost = 0
        print(visited)
        for is_visited, cost in visited:
            if is_visited is False:
                return -1
            else:
                if cost > max_cost:
                    max_cost = cost

        return max_cost


    def build_graph(self, times, node_count):
        graph = {}
        for i in range(1, node_count + 1):
            graph[i] = []

        for edge in times:
            # source : (target, cost)
            graph[edge[0]].append((edge[1], edge[2]))

        return graph

