from data_structure.bst import BST, Node


#########
# search#
#########
# root = Node(5)
#
# root.left = Node(3)
# root.right = Node(7)
#
# root.left.left = Node(2)
# root.left.left.left = Node(1)
# root.left.right = Node(4)
#
# root.right.left = Node(6)
# root.right.right = Node(10)
#
# tree = BST(root)
#
# print(tree.search(root, 5))



#########
# insert#
#########

root = Node(5)

ma_tree = BST(root)


ma_tree.add(root, Node(3))
ma_tree.add(root, Node(7))
ma_tree.add(root, Node(2))
ma_tree.add(root, Node(4))
ma_tree.add(root, Node(6))
ma_tree.add(root, Node(10))
ma_tree.add(root, Node(1))
ma_tree.add(root, Node(5))

print(ma_tree.search(ma_tree.root, 4))

result = []
ma_tree.search_range(ma_tree.root, 1, 10, result)

print(result)