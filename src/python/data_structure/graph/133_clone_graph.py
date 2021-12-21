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
        self.cloned = {}

    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None

        self._traverse(node)

        return self.graph[node.val]

    def _traverse(self, node):
        if node.val in self.visited:
            return

        self.visited[node.val] = True
        # self.graph[node.val] = copy.deepcopy(node)
        self.graph[node.val] = self._clone(node)

        for next_node in node.neighbors:
            self._traverse(next_node)

    # Essential: to avoid infinite recursion, use a memo to keep track of objects that have already been copied
    def _clone(self, node):
        if node.val in self.cloned:
            return self.cloned[node.val]

        cloned_neighbors = []
        new_node = Node(val=node.val, neighbors=cloned_neighbors)
        self.cloned[node.val] = new_node

        for adjacent_node in node.neighbors:
            if adjacent_node.val in self.cloned:
                cloned_neighbors.append(self.cloned[adjacent_node.val])
            else:
                clone = self._clone(adjacent_node)
                # clone = copy.deepcopy(adjacent_node)
                self.cloned[adjacent_node.val] = clone
                cloned_neighbors.append(clone)

        return new_node

