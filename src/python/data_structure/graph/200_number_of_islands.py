"""
力扣经典问题
https://leetcode.com/problems/number-of-islands/
https://labuladong.github.io/algo/4/31/108/

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""
from typing import List


class Solution:
    def __init__(self):
        self.island = 0
        self.visited = {}
        self.x = 0
        self.y = 0
        self.grid = None

    def numIslands(self, grid: List[List[str]]) -> int:
        self.x = len(grid[0])
        self.y = len(grid)
        self.grid = grid
        for y in range(0, self.y):
            for x in range(0, self.x):
                if (y, x) in self.visited or grid[y][x] == '0':
                    # skip
                    continue
                else:
                    self.find_island(y, x)
                    self.island += 1

        return self.island

    def find_island(self, idx_v, idx_h):
        if (idx_v, idx_h) in self.visited:
            return

        self.visited[(idx_v, idx_h)] = True
        # search in 4 different directions

        if idx_v + 1 <= self.y - 1:
            down_node = self.grid[idx_v + 1][idx_h]
            if down_node == '1':
                self.find_island(idx_v + 1, idx_h)
        if idx_v - 1 >= 0:
            up_node = self.grid[idx_v - 1][idx_h]
            if up_node == '1':
                self.find_island(idx_v - 1, idx_h)

        if idx_h + 1 <= self.x - 1:
            right_node = self.grid[idx_v][idx_h + 1]
            if right_node == '1':
                self.find_island(idx_v, idx_h + 1)

        if idx_h - 1 >= 0:
            left_node = self.grid[idx_v][idx_h - 1]
            if left_node == '1':
                self.find_island(idx_v, idx_h - 1)

input = [["1","1","1"],["0","1","0"],["1","1","1"]]

print(Solution().numIslands(input))