"""
TOP K problem, classic usage of the heap data structure
https://leetcode.com/problems/top-k-frequent-elements/
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

import heapq
from data_structure.heap import Heap


# comparator for tuple value
def comparator(a, b):
    return a[0] - b[0] < 0


def topK(input, k):
    freq_dict = dict()
    max_k_heap = Heap(size=k, comparator=comparator)

    for i in input:
        count = freq_dict.get(i)
        if count is not None:
            freq_dict[i] = count + 1
        else:
            freq_dict[i] = 1

    for item, freq in freq_dict.items():
        max_k_heap.add((freq, item))    # push in the tuple, order will be decided by the comparator

    # output
    for i in range(0, k):
        print(max_k_heap.pop[1])
