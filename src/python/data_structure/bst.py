"""
Binary search tree impl
"""
from collections import deque


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return 'value: {}, left child: {}, right child: {}'.format(self.value, self.left and self.left.value,
                                                                  self.right and self.right.value)


class BST:
    def __init__(self, root=Node()):
        self.root = root

    def search(self, root, value):
        if not root:
            return None
        if root.value == value:
            return root
        elif value < root.value:
            return self.search(root.left, value)
        elif value > root.value:
            return self.search(root.right, value)

    def add(self, root, node):
        if not root:
            return None
        if root.value >= node.value:
            if root.left:
                self.add(root.left, node)
            else:
                root.left = node

        elif root.value < node.value:
            if root.right:
                self.add(root.right, node)
            else:
                root.right = node

        return root

    def search_range(self, root, min, max, result):
        if not root:
            return result

        if root.value == min or root.value == max:
            result.append(root.value)

        if root.value > min and root.value < max:
            result.append(root.value)
            self.search_range(root.left, min, max, result)
            self.search_range(root.right, min, max, result)

        # only search right sub tree if root node is smaller than min
        if root.value <= min:
            self.search_range(root.right, min, max, result)

        # only search left sub tree if root node is bigger than max
        if root.value >= max:
            self.search_range(root.left, min, max, result)

    def traversal_inorder(self, root):
        if not root:
            return None
        self.traversal_inorder(root.left)
        print(root.value)
        self.traversal_inorder(root.right)

    def traversal_inorder_non_recursive(self, root):
        stack = deque()
        stack.appendleft(root)

        visited = []
        while True:
            try:
                current = stack.popleft()
            except IndexError:
                break

            if not current.left or current.left in visited:
                print(current)
                visited.append(current)
                continue

            if current.right:
                stack.appendleft(current.right)

            stack.appendleft(current)

            if current.left:
                stack.appendleft(current.left)

    def from_ordered_list(self, root, o_list):
        m_index = self._find_median_index(o_list)

        root.value = o_list[m_index]

        l_list = o_list[0:m_index]
        if l_list:
            root.left = self.from_ordered_list(Node(), l_list)

        r_list = o_list[m_index + 1:]
        if r_list:
            root.right = self.from_ordered_list(Node(), r_list)

        return root

    def _find_median_index(self, list):
        # int(3/2) =1
        return int(len(list) / 2)

    def pretty_print(self):
        """
        BFS
        """
        tree_height = self.height(self.root)

        bfs_queue = deque()
        print_queue = deque()

        bfs_queue.appendleft({'node': self.root, 'level': 0, 'parent': None})

        while True:
            current = None
            try:
                current = bfs_queue.pop()
            except IndexError:
                break

            print_queue.append(current)

            cur_node = current.get('node')
            cur_level = current.get('level')

            if cur_node.left:
                bfs_queue.appendleft({'node': cur_node.left, 'level': cur_level + 1, 'parent': cur_node})

            if cur_node.right:
                bfs_queue.appendleft({'node': cur_node.right, 'level': cur_level + 1, 'parent': cur_node})

        for info in print_queue:
            print(info.get('node').value, info.get('level'))

        # TODO: not sure how to calculate horizonal position
        # root_ident = '\t' * tree_height
        # _str = ''
        #
        # while True:
        #     current = None
        #     try:
        #         current = print_queue.popleft()
        #     except IndexError:
        #         break
        #
        #     cur_node = current.get('node')
        #     cur_level = current.get('level')

    def height(self, root):
        """
        get height
        :return: height of the bst
        """

        if not root:
            return 0

        return max(self.height(root.left) + 1, self.height(root.right) + 1)
