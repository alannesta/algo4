"""
Binary search tree impl
"""


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return 'root: {}, left child: {}, right child: {}'.format(self.value, self.left and self.left.value,
                                                                  self.right and self.right.value)


class BST:
    def __init__(self, root):
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


