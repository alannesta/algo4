"""
https://leetcode.com/problems/path-with-maximum-probability/

Dijkstra 模版题
"""
from typing import List
import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = self.build_graph(edges, succProb, n)
        # print(graph)
        node_heap = []
        node_tracker = [float('-inf')] * n
        # (node_id, -prob_to_node)
        heapq.heappush(node_heap, (-1, start))
        node_tracker[start] = 1 # do not forget to set start

        while node_heap:
            # (node_id, -prob_to_node)
            cur_node = heapq.heappop(node_heap)
            node_id = cur_node[1]
            prob_to_node = -cur_node[0]

            if node_id == end:
                return node_tracker[node_id]

            # !!Essential: this check could improve efficiency
            # no need to visit neighbours
            if prob_to_node < node_tracker[node_id]:
                continue

            for neb in graph[node_id]:
                chance_to_neb = neb[1] * prob_to_node
                if chance_to_neb > node_tracker[neb[0]]:
                    # update max prob
                    node_tracker[neb[0]] = chance_to_neb
                    heapq.heappush(node_heap, (-chance_to_neb, neb[0]))

        return 0

    def build_graph(self, edges, prob, n):
        graph = {}

        for i in range(n):
            graph[i] = []

        for idx, edge in enumerate(edges):
            probability = prob[idx]
            # (node_id, prob)
            graph[edge[0]].append((edge[1], probability))
            graph[edge[1]].append((edge[0], probability))

        return graph

# n = 3
# edges = [[0, 1], [1, 2], [0, 2]]
# succProb = [0.5, 0.5, 0.2]


# n = 3
# edges = [[0, 1], [1, 2], [0, 2]]
# succProb = [0.5, 0.5, 0.3]
# print(Solution().maxProbability(n, edges, succProb, 0, 2))
