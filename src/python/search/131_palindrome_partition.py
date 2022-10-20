"""
https://leetcode.com/problems/palindrome-partitioning/
"""

from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.input = []

    def partition(self, s: str) -> List[List[str]]:
        self.traverse(s, 0, "", cur_partition=[])
        return self.result

    def traverse(self, s, start_idx, cur_str, cur_partition):
        # reached end of input
        if start_idx == len(s):
            self.result.append(cur_partition[::])
            # cur_partition.pop()
            return

        for i in range(start_idx, len(s)):
            cur_str += s[i]
            if self.is_valid(cur_str):
                cur_partition.append(cur_str)
                self.traverse(s, i + 1, "", cur_partition)
                cur_partition.pop()

    def is_valid(self, str):
        i = 0
        j = len(str) - 1

        while i <= j:
            if str[i] != str[j]:
                return False
            i += 1
            j -= 1

        return True


input = "aab"

print(Solution().partition(input))
