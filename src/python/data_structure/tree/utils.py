"""
Utility functions for tree: serialize/deserialize(leetcode testcase format), visualize
"""
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({}, left: {}, right: {})'.format(self.val, self.left.val, self.right.val)


def deserialize(input_list: str):
    """

    :param input_list:
    :return:
    """
    if input_list == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in input_list.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def serialize(root: TreeNode):
    """
    serailize a tree into str(leetcode testcase format) using BFS

    :param root:
    :return:
    """
    output = []

    stack = deque()

    output.append(root.val)
    stack.append(root.left)
    stack.append(root.right)

    while stack:
        cur_node = stack.popleft()
        if cur_node:
            output.append(cur_node.val)
            stack.append(cur_node.left)
            stack.append(cur_node.right)
        else:
            output.append(None)

    # remove trailing null nodes...
    while True:
        try:
            last_elem = output[-1]
            peek_elem = output[-2]
            if last_elem is None:
                if peek_elem is None:
                    output.pop()
                # the None node is at the next level
                if len(output) % 2 == 0:
                    output.pop()
            else:
                break
        except IndexError:
            pass

    str_repr = '['

    for elem in output:
        if elem is None:
            str_repr = str_repr + 'null,'
        else:
            str_repr = str_repr + str(elem) + ','

    str_repr = str_repr[:-1] + ']'

    return str_repr


def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    import turtle
    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    # t.hideturtle()
    turtle.mainloop()


if __name__ == '__main__':
    # drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
    # drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
    drawtree(deserialize('[120,70,140,50,100,130,160,20,55,75,110,119,135,150,200]'))
    # drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
