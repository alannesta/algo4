"""
1200. Minimum Absolute Difference
https://leetcode.com/problems/minimum-absolute-difference/

OA:
https://www.1point3acres.com/bbs/thread-937337-1-1.html
"""

from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        result = []
        arr.sort()
        min_diff = arr[-1] - arr[0]

        for i in range(0, len(arr) - 1):
            j = i + 1
            if arr[j] - arr[i] < min_diff:
                min_diff = arr[j] - arr[i]
                result.clear()
                result.append([arr[i], arr[j]])
            elif arr[j] - arr[i] == min_diff:
                result.append([arr[i], arr[j]])

        return result

