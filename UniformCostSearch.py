import heapq

def ucs(graph, start, goal):
    # Priority Queue stores tuples: (current_cost, path_taken)
    pq = [(0, [start])]
    visited = set()

    while pq:
        # Pop the path with the lowest cost first
        cost, path = heapq.heappop(pq)
        node = path[-1]

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)
            # Explore neighbors
            for n, step_cost in graph.get(node, []):
                if n not in visited:
                    heapq.heappush(pq, (cost + step_cost, path + [n]))
    
    return None, float("inf")

# Graph with edge weights: 'A': [['Neighbor', Cost], ...]
graph = {
    'A': [['B', 1], ['C', 2]],
    'B': [['D', 3], ['E', 4]],
    'C': [['F', 5]],
    'D': [], 'E': [['F', 6]], 'F': []
}

result_path, result_cost = ucs(graph, 'A', 'F')
print(f"Path: {result_path}, Cost: {result_cost}")