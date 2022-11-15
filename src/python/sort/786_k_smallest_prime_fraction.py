"""
786. K-th Smallest Prime Fraction
https://leetcode.com/problems/k-th-smallest-prime-fraction/

这道题是373的克隆体, 写一下练手
"""

from typing import List
import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        min_heap = []

        # reverse iterate的方法
        for j in range(len(arr) - 1, 0, -1):
            heapq.heappush(min_heap, (arr[0] / arr[j], 0, j))

        counter = 0
        while heapq:
            cur_smallest = heapq.heappop(min_heap)
            counter += 1

            if counter == k:
                return [arr[cur_smallest[1]], arr[cur_smallest[2]]]

            if cur_smallest[1] + 1 < len(arr):
                heapq.heappush(min_heap,
                               (arr[cur_smallest[1] + 1] / arr[cur_smallest[2]], cur_smallest[1] + 1, cur_smallest[2]))
