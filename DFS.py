def dfs(graph, node, visited=None):
    """
    Depth-First Search (DFS) algorithm for graph traversal.
    
    Args:
        graph (dict): A dictionary representing the graph where keys are nodes
                     and values are lists of adjacent nodes
        node: The current node being visited
        visited (set, optional): Set of already visited nodes. Defaults to None.
    
    Returns:
        None: Prints the nodes in DFS traversal order
    """
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node, end=" ")
    
    for n in graph[node]:
        if n not in visited:
            dfs(graph, n, visited)

# Graph using Lists to maintain order
graph = {'A':['B','C'], 'B':['D','E'], 'C':['F'], 'D':[], 'E':['F'], 'F':[]}
dfs(graph, 'A')