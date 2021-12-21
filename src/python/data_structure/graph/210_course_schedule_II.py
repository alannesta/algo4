"""
https://leetcode.com/problems/course-schedule-ii/

Topological sort
"""

from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        self.has_cycle = False
        self.visited = None
        self.cur_path = None
        self.course_order = []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.visited = [False] * numCourses
        self.cur_path = [False] * numCourses

        # the hard part is building the graph with default dict
        graph = self._build_graph(prerequisites, numCourses)

        for node in graph.keys():
            self._traverse(graph, node)

        if self.has_cycle:
            return []

        return self.course_order

    def _build_graph(self, prereq, numCourses):
        graph = defaultdict(list)

        for req in prereq:
            graph[req[0]] += req[1:]

        # Essential: fill dict with values that are not present in prereq
        for i in range(numCourses):
            if i not in graph:
                graph[i] = []

        return graph

    def _traverse(self, graph, node):

        # Essential: Check for cycle before checking for visited!!
        if self.cur_path[node]:
            self.has_cycle = True
            return

        if self.visited[node] or self.has_cycle:
            return

        self.visited[node] = True
        self.cur_path[node] = True

        for neighbour in graph[node]:
            self._traverse(graph, neighbour)

        # Essential: post order traversal of graph!!!
        self.course_order.append(node)
        self.cur_path[node] = False


# 使用另一种topological sorting的算法:
# https://en.wikipedia.org/wiki/Topological_sorting
# 这种算法并不容易想到, 但是代码更为简洁. 解法的原理是每一次loop graph, 必然至少有一个节点的in order 为0(此node不再依赖其它任务)
# 将inorder为0的节点加入solution, 并从剩余node的neighbour里移除此node, 然后再一次遍历graph
class SolutionII:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_order = []

        graph = self._build_graph(prerequisites, numCourses)

        # print(graph)

        while graph:
            remain_nodes = list(graph.keys())
            acyclic = False
            removed = []
            for node in remain_nodes:
                if not graph[node]:
                    acyclic = True
                    course_order.append(node)
                    removed.append(node)
                    del graph[node]

            if not acyclic:
                print('cycle detected: ', graph)
                return []

            for to_remove in removed:
                for node in list(graph.keys()):
                    if to_remove in graph[node]:
                        graph[node].remove(to_remove)

        return course_order

    def _build_graph(self, prereq, numCourses):
        graph = defaultdict(list)

        for req in prereq:
            graph[req[0]] += req[1:]

        # Essential: fill dict with values that are not present in prereq
        for i in range(numCourses):
            if i not in graph:
                graph[i] = []

        return graph


sol = SolutionII()

sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
