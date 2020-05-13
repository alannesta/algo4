import unittest
from data_structure.linked_list.linked_list import LinkedList
from data_structure.linked_list.double_linked_list import DELinkedList


class Test(unittest.TestCase):

    def test_api(self):
        ma_list = LinkedList()

        ma_list.add_last(1)
        ma_list.add_first(2)
        ma_list.add_first(3)
        ma_list.add_last(4)

        ma_list.add_first(4)
        ma_list.add_last(4)

        assert ma_list.get(0) == 4

        ma_list.add(4, 100)
        assert ma_list.get(4) == 100

        ma_list.remove(1)

        assert ma_list.get(3) == 100
        assert ma_list.get(1) == 2

        print(ma_list)

    def test_deque_api(self):
        ma_list = DELinkedList()

        ma_list.append_left(1)
        ma_list.append_left(2)
        ma_list.append_left(3)
        ma_list.append_right(4)
        ma_list.append_right(5)
        ma_list.append_right(6)

        assert ma_list.get(2) == 1
        assert ma_list.size == 6
        ma_list.pop_left()
        ma_list.pop_right()
        assert ma_list.size == 4
        assert ma_list.head.val == 2
        assert ma_list.tail.val == 5
        # ma_list.add(3, 100)
        ma_list.add(1, 110)
        ma_list.add(0, 111)

        assert ma_list.get(2) == 110

        ma_list.remove(0)
        assert ma_list.head.val == 2

        ma_list.append_right(1000)
        ma_list.append_left(1001)
        ma_list.remove_elem(4)
        ma_list.remove_elem(1021)
        ma_list.remove_elem(5)

        assert ma_list.get(3) == 1

        print(ma_list)
