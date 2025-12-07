def dls(graph, node, goal, limit):
    if node == goal:
        return [node]
    
    if limit <= 0:
        return None
    
    for n in graph[node]:
        # Recursive call with reduced limit
        path = dls(graph, n, goal, limit - 1)
        if path:
            return [node] + path

    return None

graph = {'A':['B','C'], 'B':['D','E'], 'C':['F'], 'D':[], 'E':['F'], 'F':[]}
print(dls(graph, 'A', 'F', 2))