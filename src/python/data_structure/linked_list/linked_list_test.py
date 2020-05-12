import unittest
from data_structure.linked_list.linked_list import LinkedList


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
