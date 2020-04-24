from data_structure.heap import Heap

# ma_heap = Heap()
#
# ma_heap.add(36)
# ma_heap.add(2)
# ma_heap.add(7)
# ma_heap.add(17)
# ma_heap.add(19)
# ma_heap.add(100)
# ma_heap.add(1)
# ma_heap.add(25)
# ma_heap.add(3)
# ma_heap.add(101)
#
# print(ma_heap._heap_arr)
# print(ma_heap.pop_max())
# print(ma_heap._heap_arr)
# print(ma_heap.pop_max())
# print(ma_heap._heap_arr)

empty_heap = Heap()

i_list = [2, 3, 5, 23, 21, 11, 10, 19, 8]

empty_heap._heap_arr = i_list
empty_heap.heapify_v2()

print(empty_heap._heap_arr)
