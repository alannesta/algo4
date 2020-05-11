import unittest
from data_structure.linked_list.linked_list import LinkedList, Node


class Test(unittest.TestCase):

    def test_api(self):
        ma_list = LinkedList()

        print(ma_list)
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        ma_list.add_last(node1)
        ma_list.add_last(node2)
        ma_list.add_last(node3)
        print(ma_list)
        ma_list.add_first(node4)
        ma_list.add_first(node4)
        ma_list.add_first(node4)
        print(ma_list)
        print(ma_list.get(0))

        ma_list.add(4, Node(100))
        print(ma_list.get(4))

        ma_list.remove(1)

        print(ma_list)
