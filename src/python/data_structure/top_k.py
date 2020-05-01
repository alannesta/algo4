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
    max_k_heap = Heap(size_limit=k, comparator=comparator)

    for i in input:
        count = freq_dict.get(i)
        if count is not None:
            freq_dict[i] = count + 1
        else:
            freq_dict[i] = 1

    print(freq_dict)
    for item, freq in freq_dict.items():
        if max_k_heap.size < k or max_k_heap.peek()[0] < freq:
            max_k_heap.push((freq, item))  # push in the tuple, order will be decided by the comparator


    # output
    for i in range(0, k):
        print(max_k_heap.pop()[1])


input = [1, 1, 2, 3, 3, 3, 4, 5, 6, 6, 6, 6, 8, 7, 5, 5, 5, 5]
topK(input, 3)
