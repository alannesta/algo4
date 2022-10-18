"""
https://leetcode.com/problems/max-area-of-island/
和LC200: number of islands 类似
核心思路: 使用DFS的思想搜索二维数组.
DFS和回溯并不是必然一起出现的.
DFS的过程中记录相关路径需要回溯, 但是这道题目是在遍历的过程中记录count(island area), 并不需要回溯. 记录count可以通过公共变量的方法, 也
可以通过使用函数返回值的方法
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

# 使用return value的解法, 减少公共变量
class Solution2:
    def __init__(self):
        self.grid = None
        # 小技巧: direction函数, 代码更为简洁
        self.directions = [
            [-1, 0], [1, 0], [0, -1], [0, 1]
        ]
        self.visited = {}
        self.y = 0
        self.x = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.y = len(grid)
        self.x = len(grid[0])
        self.grid = grid
        max_area = 0

        for j in range(self.y):
            for i in range(self.x):
                if (j, i) in self.visited or grid[j][i] == 0:
                    continue
                else:
                    i_area = self.traverse(j, i)
                    max_area = max(max_area, i_area)

        return max_area

    # traverse函数返回从idx_y, idx_x起遍历的数值为1的节点的个数
    def traverse(self, idx_y, idx_x) -> int:

        # 边界条件检查的两种方式：
        # 1. 遍历前检查
        # 2. 遍历函数开始时检查. 此处用这种方式代码更为简洁.
        if idx_y < 0 or idx_y > self.y - 1 or idx_x < 0 or idx_x > self.x - 1:
            return 0

        if (idx_y, idx_x) in self.visited:
            return 0

        cur_area = 0

        if self.grid[idx_y][idx_x] == 1:
            cur_area += 1
            self.visited[(idx_y, idx_x)] = True
            for direction in self.directions:
                cur_area += self.traverse(idx_y + direction[0], idx_x + direction[1])

        return cur_area
