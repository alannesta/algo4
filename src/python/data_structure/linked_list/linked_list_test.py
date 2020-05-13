import unittest
from data_structure.linked_list.linked_list import LinkedList
from data_structure.linked_list.double_linked_list import DELinkedList


class Test(unittest.TestCase):

    def test_api(self):
        ma_list = LinkedList()

        print(ma_list)

        ma_list.add_last(1)
        print(ma_list)
        ma_list.add_first(2)
        ma_list.add_first(3)
        ma_list.add_last(4)

        ma_list.add_first(4)
        ma_list.add_last(4)

        print(ma_list)
        print(ma_list.get(0))

        ma_list.add(4, 100)
        print(ma_list.get(4))

        ma_list.remove(1)

        print(ma_list)

    def test_deque_api(self):
        ma_list = DELinkedList()

        ma_list.append_left(1)
        ma_list.append_left(2)
        ma_list.append_left(3)
        ma_list.append_right(4)
        ma_list.append_right(5)
        ma_list.append_right(6)

        print(ma_list)
        print(ma_list.get(2))
        assert ma_list.size == 6
        ma_list.pop_left()
        ma_list.pop_right()
        assert ma_list.size == 4
        print(ma_list)
        # ma_list.add(3, 100)
        ma_list.add(1, 110)
        ma_list.add(0, 111)
        print(ma_list)
        ma_list.remove(0)
        print(ma_list)
        # print(ma_list.get(0))
        #
        # ma_list.add(4, 100)
        # print(ma_list.get(4))
        #
        # ma_list.remove(1)
        #
        # print(ma_list)
