"""
https://leetcode.com/problems/all-paths-from-source-to-target/

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i

(i.e., there is a directed edge from node i to node graph[i][j]).

"""

from typing import List


class Solution:
    def __init__(self):
        self.all_paths = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        cur_path = [0]

        self._traverse(graph, 0, cur_path)

        return self.all_paths

    # 对比DFS遍历框架
    def _traverse(self, graph, node, cur_path):
        if node == len(graph) - 1:
            self.all_paths.append(cur_path[:])
            return

        for n in graph[node]:
            cur_path.append(n)
            self._traverse(graph, n, cur_path)
            cur_path.pop()
