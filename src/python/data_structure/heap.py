"""
Max heap impl
"""
import math
import copy

class Heap:
    def __init__(self, size=None):
        self._heap_arr = []

    def heapify(self, input_list):
        """
        in-place heapify
        """
        self._heap_arr = copy.copy(input_list)
        idx = 1
        while idx <= len(input_list) - 1:
            self._bubble_up(idx)
            idx = idx + 1

    def add(self, value):
        self._heap_arr.append(value)
        self._bubble_up(len(self._heap_arr) - 1)

    def pop_max(self):
        self._swap(0, len(self._heap_arr) - 1)

        max_val = self._heap_arr.pop()

        self._sift_down()  # re-balance by sift down the root node

        return max_val

    def _bubble_up(self, index):
        while index > 0:
            parent_index = self._find_parent(index)

            if self._heap_arr[index] > self._heap_arr[parent_index]:
                self._swap(index, parent_index)
                index = parent_index

            else:
                break

    def _sift_down(self):
        current_idx = 0
        heap_size = len(self._heap_arr) - 1
        while True:
            l_child_idx = current_idx * 2 + 1
            r_child_idx = current_idx * 2 + 2

            if l_child_idx > heap_size:
                break

            if l_child_idx == heap_size and self._heap_arr[l_child_idx] > self._heap_arr[current_idx]:
                self._swap(current_idx, l_child_idx)
                break

            if r_child_idx <= heap_size:

                if self._heap_arr[l_child_idx] >= self._heap_arr[r_child_idx]:
                    max_idx = l_child_idx
                else:
                    max_idx = r_child_idx

                if self._heap_arr[max_idx] > self._heap_arr[current_idx]:
                    self._swap(max_idx, current_idx)
                    current_idx = max_idx
                else:
                    break

    def _find_parent(self, index):
        if index == 0:
            return 0

        if index % 2 == 0:
            parent_index = index / 2 - 1

        if index % 2 == 1:
            parent_index = (index - 1) / 2

        return int(parent_index)

    def _swap(self, idx1, idx2):
        temp = self._heap_arr[idx1]
        self._heap_arr[idx1] = self._heap_arr[idx2]
        self._heap_arr[idx2] = temp
