from collections import deque


def bfs(graph, start):
    """
    Breadth-First Search (BFS)
    graph: dictionary where keys are nodes and values are lists of neighbors
    returns: list of nodes in the order they were visited
    """
    visited = set()
    order = []
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def dfs(graph, start):
    """
    Depth-First Search (DFS)
    graph: dictionary where keys are nodes and values are lists of neighbors
    returns: list of nodes in the order they were visited
    """
    visited = set()
    order = []

    def _dfs(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                _dfs(neighbor)

    _dfs(start)
    return order
