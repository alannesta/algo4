from data_structure.heap import Heap


# ma_heap = Heap()
#
# ma_heap.push(36)
# ma_heap.push(2)
# ma_heap.push(7)
# ma_heap.push(17)
# ma_heap.push(19)
# ma_heap.push(100)
# ma_heap.push(1)
# ma_heap.push(25)
# ma_heap.push(3)
# ma_heap.push(101)
#
# print(ma_heap._heap_arr)
# print(ma_heap.pop())
# print(ma_heap._heap_arr)
# print(ma_heap.pop())
# print(ma_heap._heap_arr)

# min heap
def comparator(a, b):
    return a - b > 0

# heap with size limit
empty_heap = Heap(size_limit=10, comparator=comparator)

i_list = [23, 2, 3, 5, 21, 11, 10, 19, 8]

empty_heap._heap_arr = i_list
# empty_heap.heapify_v2()
empty_heap.heapify_optimize(i_list)

print(empty_heap._heap_arr)
empty_heap.push(9)
empty_heap.push(15)
print(empty_heap._heap_arr)

##############
# stdlib heapq
##############
# heapq.heapify(i_list)
# print(i_list)
