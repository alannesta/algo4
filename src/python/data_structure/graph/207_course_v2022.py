"""
https://leetcode.com/problems/course-schedule/

DAG环的检测
2022 refresh
"""
from typing import List
from collections import defaultdict, deque


class Solution:
    # solution 1: recommended: BFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

        return counter == numCourses

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

    # solution 2: DFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited = [False] * numCourses
        on_path = [False] * numCourses
        self.graph = self.build_graph(prerequisites)

        for course in self.graph.keys():
            self.traverse(course, on_path)

        return self.can_finish

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
        on_path[course] = False

    def build_graph(self, prerequisites):
        graph = defaultdict(list)
        for dep in prerequisites:
            # key(prerequisite) -> values(dependents): values depends on key to finish
            graph[dep[1]].append(dep[0])

        return graph
