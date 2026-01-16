def bfs(graph, node):
    """
    Breadth-First Search (BFS) algorithm for graph traversal.
    
    Args:
        graph (dict): A dictionary representing the graph where keys are nodes
                     and values are lists of adjacent nodes
        node: The starting node for the traversal
    
    Returns:
        None: Prints the nodes in BFS traversal order
    """
    visited, queue = [node], [node]
    
    while queue:
        m = queue.pop(0) 
        print(m, end=" ")
        
        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

graph = {'A':['B','C'], 'B':['D','E'], 'C':['F'], 'D':[], 'E':['F'], 'F':[]}
bfs(graph, 'A')