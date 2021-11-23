"""
https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the

array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""
from typing import List
import heapq

from collections import deque


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        O(NlogN) solution, using tombstone marker without poping from heap
        please note that heapq support pushing list of item, first item in list will be used for comparison
        :param nums:
        :param k:
        :return:
        """
        max_heap = []
        item_dict = {}
        result = []

        for i in range(len(nums)):
            item = [-nums[i], False]
            heapq.heappush(max_heap, item)

            if nums[i] not in item_dict:
                item_dict[nums[i]] = [item]
            else:
                item_dict[nums[i]].append(item)

            if i - k >= 0:
                # "remove" element from heap
                item_to_remove = nums[i - k]

                in_heap_item = item_dict[item_to_remove].pop()
                in_heap_item[1] = True  # mark as removed

                while max_heap[0][1] is True:
                    heapq.heappop(max_heap)

                result.append(-max_heap[0][0])
            if i == k - 1:
                # handle the first window
                result.append(-max_heap[0][0])

        return result

    def maxSlidingWindow_v2(self, nums: List[int], k: int) -> List[int]:
        """
        O(N) solution, using mono queue
        :param nums:
        :param k:
        :return:
        """
        m_queue = deque()
        result = []

        for i in range(len(nums)):
            while m_queue and m_queue[-1] < nums[i]:
                m_queue.pop()
            m_queue.append(nums[i])

            if i - k >= 0:
                item_to_remove = nums[i - k]

                if item_to_remove == m_queue[0]:
                    m_queue.popleft()

            if i >= k - 1:
                result.append(m_queue[0])

        return result
