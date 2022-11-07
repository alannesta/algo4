"""
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

from typing import List


# 更为优化的解:
# https://labuladong.github.io/algo/4/31/110/
class Solution:
    def __init__(self):
        self.result = []
        self.pool = []
        self.used = []

    def generateParenthesis(self, n: int) -> List[str]:
        for i in range(n):
            self.pool.append("(")
            self.pool.append(")")

        self.used = [0] * len(self.pool)

        self.traverse([])
        return self.result

    # 和LC47 permutation unique相似的两层去重思路(剪枝)
    # 额外加入is_valid的判定进行剪枝(类似n皇后, 数独)
    # 最原始的暴力解法可以设计为先进性全排列, 再在全排列里进行is_valid的筛选, 当然会超时
    def traverse(self, cur_path):
        if len(cur_path) == len(self.pool):
            self.result.append("".join(cur_path))
            return

        chosen = set()
        for i in range(len(self.pool)):
            if self.used[i] or self.pool[i] in chosen:
                continue

            if self.is_valid(cur_path, self.pool[i]):
                cur_path.append(self.pool[i])
                self.used[i] = 1
                chosen.add(self.pool[i])
                self.traverse(cur_path)
                self.used[i] = 0
                cur_path.pop()

    def is_valid(self, cur_path, next):
        if next == "(":
            return True

        if next == ")":
            c = cur_path[:]
            open_count = 0
            close_count = 0
            while c:
                if c.pop() == "(":
                    open_count += 1
                else:
                    close_count += 1

            return open_count > close_count
