"""
Generic binary search util which mimics the functionality of the "bisect" module in standard lib
"""

"""
Return the index where to insert item x in input_list, assuming input_list is sorted.

The return value i is such that all e in input_list[:i] have e < x, and all e in
input_list[i:] have e >= x.  So if x already appears in the list, input_list.insert(x) will
insert just before the leftmost x already there.
"""


def bisect(input_list, elem):
    start = 0
    end = len(input_list) - 1

    while end >= start:
        mid = (end + start) // 2

        if elem > input_list[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return start

def bisect_template2(input_list, elem):
    start = 0
    end = len(input_list) - 1

    while end > start:
        mid = (end + start) // 2

        if elem > input_list[mid]:
            start = mid + 1
        else:
            end = mid

    return start

# kaka = [1, 2, 2, 3, 3, 3, 3, 5]
#
# print(bisect(kaka, 3))
# print(bisect_template2(kaka, 3))
