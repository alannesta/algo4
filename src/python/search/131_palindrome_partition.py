"""
https://leetcode.com/problems/palindrome-partitioning/
"""

from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.input = []

    def partition(self, s: str) -> List[List[str]]:
        self.traverse(s, 0, cur_partition=[])
        return self.result

    def traverse(self, s, start_idx, cur_partition):
        # reached end of input
        if start_idx == len(s):
            self.result.append(cur_partition[::])
            return

        for i in range(start_idx, len(s)):
            if self.is_valid(s[start_idx: i + 1]):
                cur_partition.append(s[start_idx: i + 1])
            else:
                continue
            self.traverse(s, i + 1, cur_partition)
            cur_partition.pop()

    def is_valid(self, str):
        if not str:
            return False

        if len(str) == 1:
            return True

        if str == str[::-1]:
            return True

        return False


input = "aab"

print(Solution().partition(input))
