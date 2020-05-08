"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""
import math


class SlidingWindowMaximum:
    def __init__(self, input_list, window_size):
        self.input_list = input_list
        self.window_size = window_size
        self.current_window = []
        self.cur_window_start = 0
        self.current_max = [-math.inf, 1]  # (max number: count)
        self._init_window()

    def max(self):
        return self.current_max[0]

    def slide(self):
        self._remove_from_window()
        self._add_to_window()

    def _init_window(self):
        self.current_window = self.input_list[self.cur_window_start: self.window_size]
        for num in self.current_window:
            if num == self.current_max[0]:
                self.current_max[1] += 1

            if num > self.current_max[0]:
                self.current_max = [num, 1]

    def _remove_from_window(self):
        if len(self.current_window) > 0:
            poped = self.current_window.pop(0)
            if poped == self.current_max[0]:
                self.current_max[1] -= 1

                # refind the max
                if self.current_max[1] == 0:
                    self._init_window()
        else:
            print('end of window')

    def _add_to_window(self):
        if self.cur_window_start + self.window_size <= len(self.input_list) - 1:
            appended = self.input_list[self.cur_window_start + self.window_size]

            self.current_window.append(appended)
            if appended > self.current_max[0]:
                self.current_max = [appended, 1]

            if appended == self.current_max[0]:
                self.current_max[1] += 1

        self.cur_window_start += 1


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

swm = SlidingWindowMaximum(nums, k)

print(swm.max())
swm.slide()
print(swm.max())
swm.slide()
print(swm.max())
swm.slide()
print(swm.max())
swm.slide()
print(swm.max())
swm.slide()
print(swm.max())
swm.slide()
print(swm.max())
swm.slide()