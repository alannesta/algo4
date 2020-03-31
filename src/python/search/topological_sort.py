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

"""

# import copy

graph = dict()

graph[0] = [2]
graph[1] = [2, 3]
graph[2] = [4]
graph[3] = [4]
graph[4] = [5, 6]
graph[5] = []
graph[6] = []

visited = []
sorted = []
visiting = []


def topological(graph, node):
    if node in visited:
        return

    if node in visiting:
        raise Exception('cycle find in graph')

    neighbours = get_neighbours(graph, node)

    visiting.append(node)

    for child_node in neighbours:
        topological(graph, child_node)

    visiting.pop()

    visited.append(node)

    sorted.insert(0, node)


def get_neighbours(graph, node):
    return graph.get(node)


if __name__ == "__main__":
    for node in graph.keys():
        topological(graph, node)
    print(sorted)
