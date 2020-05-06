"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].
"""


class SlidingWindowMedian:
    def __init__(self, input_list, window_size):
        self.input_list = input_list
        self.window_size = window_size
        self.cur_window_start = 0
        self.current_window = []
        self.init_window()  # init the first window

    def median(self):
        if self.window_size % 2 == 0:
            return (self.current_window[self.window_size >> 1] + self.current_window[(self.window_size >> 1) - 1]) / 2
        else:
            return self.current_window[self.window_size >> 1]

    def init_window(self):
        self.current_window = sorted(self.input_list[self.cur_window_start: self.window_size])

    def slide(self):
        self._remove_from_window(self.input_list[self.cur_window_start])
        self._add_to_window(self.input_list[self.cur_window_start + self.window_size])
        self.cur_window_start += 1

    def _remove_from_window(self, elem):
        idx = self.current_window.index(elem)

        while idx < len(self.current_window) - 1:
            self.current_window[idx] = self.current_window[idx + 1]
            idx += 1

        self.current_window[-1] = None

    def _add_to_window(self, elem):
        # put the elem as the last elem of the window, which should have been set to None already
        # self.current_window[-1] = elem
        elem_idx = len(self.current_window) - 2

        # find the insertion point
        while elem_idx >= 0:
            if self.current_window[elem_idx] > elem:
                elem_idx -= 1
            else:
                break

        insert_idx = elem_idx + 1  # insert to the next position

        m_idx = len(self.current_window) - 1
        while m_idx > insert_idx:
            self.current_window[m_idx] = self.current_window[m_idx - 1]
            m_idx -= 1

        self.current_window[insert_idx] = elem


kaka = [1, 3, -1, -3, 5, 3, 6, 7]
window = 3
slide_median = SlidingWindowMedian(kaka, window)

print(slide_median.median())
slide_median.slide()
print(slide_median.median())
slide_median.slide()
print(slide_median.median())
slide_median.slide()
print(slide_median.median())
slide_median.slide()
print(slide_median.median())
slide_median.slide()
print(slide_median.median())