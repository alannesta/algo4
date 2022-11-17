"""
https://leetcode.com/problems/course-schedule-ii/

Topological sort
2022 refresh
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]):
        graph = self.build_graph(prerequisites)
        inorder = defaultdict(int)
        result = []
        counter = 0
        course_under_process = deque()

        # initialize all courses with inorder 0
        for i in range(numCourses):
            inorder[i] = 0

        for dependents in graph.values():
            for course in dependents:
                inorder[course] += 1

        for course in inorder.keys():
            if inorder[course] == 0:
                course_under_process.appendleft(course)

        while course_under_process:
            resolved_course = course_under_process.pop()
            result.append(resolved_course)
            counter += 1

            # essential: update dependent course inorder counter
            # if inorder is 0, it means no more other courses depend on this course
            # it could be put in the result
            for course in graph[resolved_course]:
                inorder[course] -= 1
                if inorder[course] == 0:
                    course_under_process.appendleft(course)

        if counter == numCourses:
            return result
        else:
            return []

    def build_graph(self, prerequisites):
        graph = defaultdict(list)
        for dep in prerequisites:
            # key(prerequisite) -> values(dependents): values depends on key to finish
            graph[dep[1]].append(dep[0])

        return graph


class Solution2:
    def __init__(self):
        self.can_finish = True
        self.visited = None
        self.graph = None
        self.result = []

    # solution 2: DFS
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]):
        self.visited = [False] * numCourses
        on_path = [False] * numCourses
        self.graph = self.build_graph(numCourses, prerequisites)

        for course in self.graph.keys():
            self.traverse(course, on_path)

        if not self.can_finish:
            return []

        return self.result[::-1]

    def traverse(self, course, on_path):
        if not self.can_finish:
            return

        if on_path[course]:
            self.can_finish = False
            return

        if self.visited[course]:
            return

        self.visited[course] = True
        on_path[course] = True
        if course in self.graph:
            for dep in self.graph[course]:
                self.traverse(dep, on_path)
        self.result.append(course)
        on_path[course] = False

    def build_graph(self, nums, prerequisites):
        graph = {}
        # 坑, 这里需要完全初始化graph!
        for i in range(nums):
            graph[i] = []
        for dep in prerequisites:
            # key(prerequisite) -> values(dependents): values depends on key to finish
            graph[dep[1]].append(dep[0])

        return graph
