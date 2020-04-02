"""
topological sort:

L ← Empty list that will contain the sorted nodes
while exists nodes without a permanent mark do
    select an unmarked node n
    visit(n)

function visit(node n)
    if n has a permanent mark then
        return
    if n has a temporary mark then
        stop   (not a DAG)

    mark n with a temporary mark

    for each node m with an edge from n to m do
        visit(m)

    remove temporary mark from n
    mark n with a permanent mark
    add n to head of L


Details:

A for loop over all the nodes on the DAG, the visited list will prevent duplicated processing (compare with DFS)

"""

# import copy
from collections import OrderedDict

graph = OrderedDict()
# graph = dict()
graph[4] = [5, 6]
graph[3] = [4]
graph[0] = [2]
graph[1] = [2, 3]
graph[6] = []
graph[2] = [4]
graph[5] = [1]


visited = []
sorted = []
visiting = []


def topological(graph, node):
    if node in visiting:
        raise Exception('cycle find in graph')

    if node in visited:
        return

    neighbours = get_neighbours(graph, node)

    # the visiting list is the extra layer above the DFS template.
    # which guards against cycles in graph. This is problem specific
    visiting.append(node)

    # we could mark as visited after the recursion as well.
    # putting it before the recursion better matches the DFS template
    visited.append(node)

    for child_node in neighbours:
        topological(graph, child_node)

    visiting.pop()

    sorted.insert(0, node)


# iterative solution (not working!!!)
# def topological_iter(graph):
#     sink_nodes = []  # a sink node is a node without out edge
#     search_stack = []
#     visited = []
#
#     for node in graph.keys():
#         print('visiting: ', node)
#         visiting = []
#         if node not in visited:
#             search_stack.append(node)
#         while len(search_stack) > 0:
#             cur_node = search_stack.pop()
#             if cur_node in visiting:
#                 raise Exception('Cycle detected on node: {}'.format(child_node))
#
#             if cur_node in visited:
#                 return
#
#             visiting.append(cur_node)
#             visited.append(cur_node)
#
#             neighbours = get_neighbours(graph, cur_node)
#
#             for child_node in neighbours:
#                 if child_node not in visited:
#                     search_stack.append(child_node)
#
#             remove_neighbour(graph, cur_node)
#             sink_nodes.insert(0, cur_node)
#
#             visiting.pop()
#
#     return sink_nodes


def topological_iter(graph):
    ordered = []
    visited = []

    while True:
        roots = get_root_node(graph)
        if len(roots) == 0:
            # when the graph is emtpy
            if len(graph.keys()) == 0:
                break
            # when the graph is not empty but no root node can be found, the there is a cycle
            else:
                raise Exception('cycle detected')

        for node in roots:
            ordered.append(node)
            visited.append(node)

            neighbours = get_neighbours(graph, node)

            for n_node in neighbours:
                if n_node in visited:
                    raise Exception('cycle detected')

            remove_parent(graph, node)
            roots.remove(node)

    return ordered


def get_root_node(graph):
    roots = []
    for key in graph.keys():
        append = True
        for neighbours in graph.values():
            if key in neighbours:
                append = False
        if append:
            roots.append(key)

    return roots


def remove_parent(graph, parent):

    del graph[parent]



def get_neighbours(graph, node):
    return graph.get(node)


def remove_neighbour(graph, node):
    graph[node] = []


if __name__ == "__main__":
    # solution 1: recursive DFS
    # for node in graph.keys():
    #     topological(graph, node)

    # solution 2: iterative DFS
    sorted = topological_iter(graph)
    # sorted = get_root_node(graph)
    print(sorted)
