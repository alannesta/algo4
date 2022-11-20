"""
743. Network Delay Time
https://leetcode.com/problems/network-delay-time/
"""
import sys
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
        # 参考787 cheapest flights里的处理
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


from collections import deque


# 体会BFS与达基萨斯的异同
class Solution_BFS:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self.build_graph(times, n)
        node_queue = deque()
        visited = [sys.maxsize] * (n + 1)  # n + 1 to avoid offset node index
        node_queue.appendleft((k, 0))
        visited[k] = 0

        while node_queue:
            elem_c = len(node_queue)
            # 这道题目不需要maintain level information, 所以这个for loop可以去掉
            # 这里为了体现BFS的模版, 保留
            for i in range(elem_c):
                cur_node = node_queue.pop()

                for adjacent_node in graph[cur_node[0]]:
                    # Essential: 寻路算法的核心: 找到cheaper的路径时作哪些处理!
                    # a cheaper route is discovered
                    if adjacent_node[1] + cur_node[1] < visited[adjacent_node[0]]:
                        visited[adjacent_node[0]] = adjacent_node[1] + cur_node[1]
                        # in this case, we add node to queue to process its neighbours
                        node_queue.appendleft((adjacent_node[0], adjacent_node[1] + cur_node[1]))
                    else:
                        # in this case, there is a faster route to adjacent node, no need to proceed with current route
                        continue

        cost = 0
        for idx in range(1, n + 1):
            if visited[idx] == sys.maxsize:
                # unreacheable node:
                return -1

            if visited[idx] > cost:
                cost = visited[idx]

        return cost

    def build_graph(self, times, node_count):
        graph = {}
        for i in range(1, node_count + 1):
            graph[i] = []

        for edge in times:
            # source : (node_id, cost)
            graph[edge[0]].append((edge[1], edge[2]))

        return graph


# times = [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]
#
# Solution_DJ().networkDelayTime(times, n=5, k=0)
# Solution_BFS().networkDelayTime(times, n=5, k=0)
