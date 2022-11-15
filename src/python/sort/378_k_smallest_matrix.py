"""
378. Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

"""
from typing import List

import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        n = len(matrix)
        counter = 0

        for i in range(n):
            # 视作n个linked list, 转为leetcode23 多路归并排序
            # 因为不是链表, 放入数组index方便接下来找到next elem
            heapq.heappush(min_heap, (matrix[i][0], i, 0))

        while min_heap:
            cur_smallest = heapq.heappop(min_heap)
            counter += 1
            if counter == k:
                return cur_smallest[0]

            if cur_smallest[2] + 1 < n:
                heapq.heappush(min_heap,
                               (matrix[cur_smallest[1]][cur_smallest[2] + 1], cur_smallest[1], cur_smallest[2] + 1))
