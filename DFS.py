def dfs(graph, node, visited=None):
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