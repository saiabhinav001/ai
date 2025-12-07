def bfs(graph, node):
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