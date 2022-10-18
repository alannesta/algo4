"""
https://leetcode.com/problems/n-queens/
N皇后问题, 我一直以来的心结...
https://www.cnblogs.com/labuladong/p/12320463.html

"""
from typing import List


class Solution:
    def __init__(self):
        self.all_boards = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = self.init_board(n)
        # backtrack如何kick start需要总结一下
        self.place_queen(board, 0)  # starting from first row
        return self.all_boards

    def init_board(self, n) -> List[List[str]]:
        board = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append('.')

            board.append(temp)

        return board

    def convert_board(self, board):
        res = []
        x = y = len(board)

        for j in range(y):
            row_str = ''
            for i in range(x):
                row_str += board[j][i]

            res.append(row_str)

        return res

    def place_queen(self, board, row_idx):
        n = len(board)
        # the last row has already been placed, which means a valid solution is found
        if row_idx >= n:
            # convert to string representation
            res = self.convert_board(board)
            self.all_boards.append(res)
            return

        row = board[row_idx]
        for col in range(n):
            # if valid, place the chess
            if self.is_valid(board, row_idx, col):
                row[col] = 'Q'
                self.place_queen(board, row_idx + 1)
                # backtrack
                row[col] = '.'
            # not valid, move on to next col, return None

    # check if placing on (row, col) is a valid solution
    def is_valid(self, board, row_idx, col_idx) -> bool:
        # n = len(board)
        # check column
        # only need to check columns above the current row
        for i in range(row_idx):
            if board[i][col_idx] == 'Q':
                return False

        return self.check_diagonal(board, row_idx, col_idx)

    def check_diagonal(self, board, row_idx, col_idx):
        n = len(board)
        # directions = [
        #     [-1, -1], [1, 1], [-1, 1], [1, -1]
        # ]
        # only two directions needs to be checked: upper left and upper right
        directions = [
            [-1, -1], [-1, 1]
        ]

        # check 4 directions
        for direction in directions:
            # check diagonally
            cur_r_idx = row_idx + direction[0]
            cur_c_dix = col_idx + direction[1]
            while 0 <= cur_r_idx <= n - 1 and 0 <= cur_c_dix <= n - 1:
                if board[cur_r_idx][cur_c_dix] == 'Q':
                    return False
                cur_r_idx += direction[0]
                cur_c_dix += direction[1]

        return True
