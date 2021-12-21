"""
https://leetcode.com/problems/clone-graph/

traverse undirected connected graph

"""
import copy


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.visited = {}
        self.graph = {}

    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None
        
        self._traverse(node)

        return self.graph[node.val]

    def _traverse(self, node):
        if node.val in self.visited:
            return

        self.visited[node.val] = True
        self.graph[node.val] = copy.deepcopy(node)

        for next_node in node.neighbors:
            self._traverse(next_node)
