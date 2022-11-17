"""
Leetcode: https://leetcode.com/problems/find-median-from-data-stream/
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.

"""

from data_structure.heap import Heap


class MedianFinder:
    def __init__(self):
        self.min_heap = Heap(comparator=lambda a, b: a - b < 0)
        self.max_heap = Heap(comparator=lambda a, b: a - b > 0)

    def add_number(self, num):
        if self.max_heap.size == 0:
            self.max_heap.push(num)
            return

        if self.min_heap.size == 0:
            self.min_heap.push(num)
            return

        r_min = self.min_heap.peek()
        l_max = self.max_heap.peek()

        if num >= r_min:
            self.min_heap.push(num)
        else:
            self.max_heap.push(num)

        self._balance()

    def median(self):
        if self.max_heap.size > self.min_heap.size:
            return self.max_heap.peek()
        elif self.min_heap.size > self.max_heap.size:
            return self.min_heap.peek()
        else:
            return (self.min_heap.peek() + self.max_heap.peek()) / 2

    def _balance(self):
        r_min_size = self.min_heap.size
        l_max_size = self.max_heap.size
        if r_min_size - l_max_size > 1:
            self.max_heap.push(self.min_heap.pop())
        elif l_max_size - r_min_size > 1:
            self.min_heap.push(self.max_heap.pop())


class MedianFinder_Bruce:
    def __init__(self):
        self.nums = []

    def add_number(self, num):
        self.nums.append(num)
        self.nums = sorted(self.nums)

    def median(self):

        size = len(self.nums)
        if size % 2 == 0:
            return (self.nums[size >> 1] + self.nums[(size >> 1) - 1]) / 2
        else:
            return self.nums[size >> 1]


median_finder = MedianFinder()
# median_finder = MedianFinder_Bruce()

median_finder.add_number(3)
median_finder.add_number(6)
median_finder.add_number(13)
median_finder.add_number(21)
median_finder.add_number(0)
median_finder.add_number(5)
median_finder.add_number(18)
median_finder.add_number(9)
median_finder.add_number(10)
median_finder.add_number(100)
# median_finder.add_number(-10)

print(median_finder.median())
