"""
heap impl
"""
import copy


# The comparator will decide min/max heap
def default_comparator(a, b):
    return a - b > 0


class Heap:
    def __init__(self, size_limit=None, comparator=None):
        self._heap_arr = []
        self.size_limit = size_limit
        self.comparator = comparator or default_comparator  # default comparator is max heap

    @property
    def size(self):
        return len(self._heap_arr)

    def heapify(self, input_list):
        """
        in-place heapify
        O(NlogN)
        """
        self._heap_arr = copy.copy(input_list)
        idx = 1
        while idx <= len(input_list) - 1:
            self._bubble_up(idx)
            idx = idx + 1

    def heapify_v2(self, start_idx=0):
        """
        O(N) by sift down approach described in:
        https://en.wikipedia.org/wiki/Heapsort
        """
        if start_idx > self.size - 1:
            return

        l_node_idx = 2 * start_idx + 1
        r_node_idx = 2 * (start_idx + 1)

        if r_node_idx <= self.size - 1:
            self.heapify_v2(l_node_idx)
            self.heapify_v2(r_node_idx)
            self._sift_down(start_idx, self.size - 1)

        elif l_node_idx <= self.size - 1:
            self.heapify_v2(l_node_idx)
            self._sift_down(start_idx, self.size - 1)

    def push(self, value):
        if self.size < self.size_limit:
            self._heap_arr.append(value)
            self._bubble_up(self.size - 1)
        else:
            self.pop_push(value)


    def pop(self):
        self._swap(0, self.size - 1)

        val = self._heap_arr.pop()

        self._sift_down(0, self.size - 1)  # re-balance by sift down the root node

        return val

    def pop_push(self, new_val):
        pop_val = self._heap_arr[0]
        self._heap_arr[0] = new_val
        self._sift_down(0, self.size - 1)  # re-balance by sift down the root node

        return pop_val

    def peek(self):
        return self._heap_arr[0]

    def _bubble_up(self, index):
        while index > 0:
            parent_index = self._find_parent(index)

            if self.comparator(self._heap_arr[index], self._heap_arr[parent_index]):
                self._swap(index, parent_index)
                index = parent_index

            else:
                break

    def _sift_down(self, start_idx, end_idx):
        current_idx = start_idx
        heap_size = end_idx
        while True:
            l_child_idx = current_idx * 2 + 1
            r_child_idx = current_idx * 2 + 2

            if l_child_idx > heap_size:
                break

            if l_child_idx == heap_size:
                if self.comparator(self._heap_arr[l_child_idx], self._heap_arr[current_idx]):
                    self._swap(current_idx, l_child_idx)
                break

            if r_child_idx <= heap_size:

                if not self.comparator(self._heap_arr[r_child_idx], self._heap_arr[l_child_idx]):
                    swap_target_idx = l_child_idx
                else:
                    swap_target_idx = r_child_idx

                if self.comparator(self._heap_arr[swap_target_idx], self._heap_arr[current_idx]):
                    self._swap(swap_target_idx, current_idx)
                    current_idx = swap_target_idx
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

    # def _find_sub_tree_range(self, root_idx):
    #     if 2 * (root_idx + 1) <= self.size - 1:
    #         return 2 * (root_idx + 1)
    #
    #     elif 2 * root_idx + 1 <= self.size - 1:
    #         return 2 * root_idx + 1
    #
    #     else:
    #         return root_idx
