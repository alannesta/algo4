"""
https://leetcode.com/problems/max-area-of-island/
和LC200: number of islands 类似
"""
from typing import List


class Solution:
    def __init__(self):
        self.max_area = 0
        self.grid = None
        self.directions = [
            [-1, 0], [1, 0], [0, -1], [0, 1]
        ]
        self.visited = {}
        self.y = 0
        self.x = 0
        self.cur_area = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.y = len(grid)
        self.x = len(grid[0])
        self.grid = grid

        for j in range(self.y):
            for i in range(self.x):
                if (j, i) in self.visited or grid[j][i] == 0:
                    continue
                else:
                    self.traverse(j, i)
                    self.max_area = max(self.max_area, self.cur_area)
                    self.cur_area = 0

        return self.max_area

    def traverse(self, idx_y, idx_x):

        if idx_y < 0 or idx_y > self.y - 1 or idx_x < 0 or idx_x > self.x - 1:
            return

        if (idx_y, idx_x) in self.visited:
            return

        if self.grid[idx_y][idx_x] == 1:
            self.visited[(idx_y, idx_x)] = True
            self.cur_area += 1
            for direction in self.directions:
                self.traverse(idx_y + direction[0], idx_x + direction[1])
