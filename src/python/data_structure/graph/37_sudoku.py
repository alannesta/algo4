"""
https://leetcode.com/problems/sudoku-solver/
leetcode经典系列, 解数独
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board, 0, 0)

    def solve(self, board, row_idx, col_idx):
        # reach end of a row, jump to next row
        if col_idx == 9:
            if row_idx < 8:
                col_idx = 0
                row_idx = row_idx + 1
            else:
                return True

        if board[row_idx][col_idx] == ".":
            # 如何处理找不到解法的情况? 如何回溯?
            for solution in range(1, 10):
                if self.is_valid(solution, row_idx, col_idx, board):
                    board[row_idx][col_idx] = str(solution)
                    # solve next col
                    found = self.solve(board, row_idx, col_idx + 1)
                    # !!! solution already found, do not backtrack, return all the way to the bottom of stack
                    # use this technique to solve problems that only need to find 1 solution
                    if found:
                        return True
                    # back track
                    board[row_idx][col_idx] = "."
            # !!! no solution found, function will return None, this will cause the backtrack
            # self.solve(board, row_idx, col_idx - 1)  # this is NOT needed!
        else:
            found = self.solve(board, row_idx, col_idx + 1)
            if found:
                return True

        return False

    def is_valid(self, num, row_idx, col_idx, board):
        # check row
        # if num in board[row_idx][0:col_idx] or num in board[row_idx][col_idx + 1:]:
        #     return False
        for i in range(9):
            if i != col_idx and board[row_idx][i] == str(num):
                return False
        # check col
        for i in range(9):
            if i != row_idx and board[i][col_idx] == str(num):
                return False

        # check 3x3 tile
        return self.check_tile(num, row_idx, col_idx, board)

    def check_tile(self, num, row_idx, col_idx, board):
        horizontal_start = col_idx // 3
        vertical_start = row_idx // 3

        for i in range(horizontal_start * 3, horizontal_start * 3 + 3):
            for j in range(vertical_start * 3, vertical_start * 3 + 3):
                if i == col_idx and j == row_idx:
                    continue
                elif board[j][i] == str(num):
                    return False

        return True


test = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

Solution().solveSudoku(test)

print(test)
